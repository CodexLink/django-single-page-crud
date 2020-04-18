import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, FormView)
from django.views.generic.base import TemplateView
from weasyprint import CSS, HTML

from .forms import *
from .models import *

template_RequiredEncapped = "elemInstanceViewer.html"
template_RequiredNoContext = "noContextResponseOnly.html"
template_pdfRenderer = "pdfRenderer.html"

# ! Source Solution for Two Forms at the same time
# - https://krzysztofzuraw.com/blog/2016/two-forms-one-view-django.html

class DataView(LoginRequiredMixin, TemplateView):
    success_url = reverse_lazy('data_user_view')
    template_name = template_RequiredEncapped

    redirect_field_name = reverse_lazy('deauth_user_view')
    model = UserTasks

    more_context = {
        "ClassInstance": str(__qualname__)
    }

    def get(self, *args, **kwargs):
        current_user = self.request.user
        form_context = super(DataView, self).get_context_data(**kwargs)
        form_context['user_instance_name'] = '%s %s %s' % (current_user.first_name, current_user.middle_name if current_user.middle_name is not None else '', current_user.last_name)
        form_context['ClassInstance'] = self.more_context['ClassInstance']
        form_context['DataSets'] = UserTasks.objects.filter(Task_Owner=self.request.user.uuid)

        form_context["AddData_Form"] = UserTaskAdditionForm(self.request.GET)
        form_context["UpdateData_Form"] = UserTaskUpdateForm(self.request.GET)

        return self.render_to_response(form_context)

    def handle_no_permission(self):
        self.raise_exception = self.request.user.is_authenticated
        if self.raise_exception:
            messages.error(self.request, "InsufficientPermission")
        else:
            messages.error(self.request, "PermissionAccessDenied")
        return super(DataView, self).handle_no_permission()

class UserAuthView(LoginView):
    template_name = template_RequiredEncapped
    form_class = AuthForm
    success_url = reverse_lazy('data_user_view')
    redirect_authenticated_user = True

    more_context = {
        "ClassInstance": str(__qualname__),
    }

    def get_context_data(self, **kwargs):
       view_context = super(UserAuthView, self).get_context_data(**kwargs)
       view_context['ClassInstance'] = self.more_context['ClassInstance']

       return view_context

    def get_success_url(self):
        return self.success_url

class UserDeauthView(LoginRequiredMixin, LogoutView):
    template_name = template_RequiredEncapped
    login_url = reverse_lazy('auth_user_view')
    next_page = login_url

    def dispatch(self, request):
        if request.user.is_authenticated:
           messages.success(self.request, "UserLoggedOut")
           print("UserLoggedOut")
        return super(UserDeauthView, self).dispatch(request)

    def handle_no_permission(self):
       messages.error(self.request, "UserAlreadyLoggedOut")
       print("UserAlreadyLoggedOut")
       return super(UserDeauthView ,self).handle_no_permission()

class DataAddition(LoginRequiredMixin, FormView):
    template_name = template_RequiredEncapped
    success_url = reverse_lazy('data_user_view')

    def dispatch(self, request):
        if not request.user.is_authenticated:
           messages.error(self.request, "UserNotLoggedIn")
           print("UserNotLoggedIn")
        return super(DataAddition, self).dispatch(request)

    def post(self, request, *args, **kwargs):
        targetFormData = UserTaskAdditionForm(request.POST)

        if targetFormData.is_valid():
            self.object = targetFormData.save(commit=False)
            self.object.Task_Owner = UserCredentials.objects.get(uuid=self.request.user.uuid)
            self.object.save()
            messages.success(self.request, "NewDataSavedSuccessfully")
        else:
            messages.error(self.request, "NewDataNotSaving")

        return redirect(self.success_url)

class DataDeletion(LoginRequiredMixin, CreateView):
    template_name = template_RequiredEncapped
    success_url = reverse_lazy('data_user_view')

    def dispatch(self, request):
        if not request.user.is_authenticated:
           messages.error(self.request, "UserNotLoggedIn")
           print("UserNotLoggedIn")
        return super(DataDeletion, self).dispatch(request)

class DataUpdate(LoginRequiredMixin, FormView):
    template_name = template_RequiredEncapped
    success_url = reverse_lazy('data_user_view')

    def dispatch(self, request):
        if not request.user.is_authenticated:
           messages.error(self.request, "UserNotLoggedIn")
           print("UserNotLoggedIn")
        return super(DataUpdate, self).dispatch(request)

    def post(self, request, *args, **kwargs):
        targetFormData = UserTaskUpdateForm(request.POST)
        if targetFormData.is_valid():
            print(request.POST)
            print("Updating")
            self.object = UserTasks.objects.filter(Task_Owner__uuid=self.request.user.uuid, Task_UUID=request.POST["TaskReferenceID"]).update(Task_Name=request.POST['Task_Name'], Task_Type=request.POST['Task_Type'], Task_Description=request.POST['Task_Description'], Task_StartTime=request.POST['Task_StartTime'], Task_EndTime=request.POST['Task_EndTime'])
            messages.success(self.request, "NewDataSavedSuccessfully")
        else:
            print(request.POST)
            print("Not valid")
            print(targetFormData.errors)
            messages.error(self.request, "NewDataNotSaving")

        return redirect(self.success_url)


class ExplicitActions(TemplateView):
    Action = None
    ItemUUID = None
    template_name = template_RequiredEncapped

    def get(self, *args, **kwargs):
        if self.Action:
            # ! Source
            ## https://simpleisbetterthancomplex.com/tutorial/2016/08/08/how-to-export-to-pdf.html

            pdfFileName = '%s_%s.pdf' % (self.request.user.username, datetime.datetime.now().strftime("%H%M%S%m%d%Y"))

            if self.Action == "ExportAll":
                html_string = render_to_string(template_pdfRenderer, {'DataSets': UserTasks.objects.filter(Task_Owner=self.request.user.uuid)})
                html = HTML(string=html_string).write_pdf(target='userdata/ExportedPDFs/%s' % (pdfFileName), stylesheets=[CSS('CrudSimulation\static\css\material.min.css'), CSS('CrudSimulation\static\css\sc_require-min.css')]);
                fs = FileSystemStorage('')

                with fs.open("userdata/ExportedPDFs/" + pdfFileName) as pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % (pdfFileName)
                    return response

                return HttpResponseRedirect(reverse('data_user_view'))

            elif "Delete" in self.Action:
                try:
                    if "All" in self.Action:
                        UserTasks.objects.all().delete()
                        messages.success(self.request, "DeletionSuccess")
                    else:
                        UserTasks.objects.filter(Task_UUID=self.kwargs['dataAttached']).delete()
                        messages.success(self.request, "DeletionSuccess")

                except:
                    messages.error(self.request, "DeletionFailed")

                finally:
                    return HttpResponseRedirect(reverse('data_user_view'))

        else:
            print("No other such candidate!")
            messages.error(self.request, "")


class UserRegistrationView(CreateView):
    template_name = template_RequiredEncapped
    form_class = RegistrationForm
    login_url = reverse_lazy('auth_user_view')

    more_context = {
        "ClassInstance": str(__qualname__)
    }

    def get_context_data(self, **kwargs):
        view_context = super(UserRegistrationView, self).get_context_data(**kwargs)
        view_context['ClassInstance'] = self.more_context['ClassInstance']
        return view_context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()

        return super().form_valid(form)


    def get_success_url(self):
        messages.success(self.request, "RegisterSuccess")
        return self.login_url
