from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, ListView, RedirectView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from requests.exceptions import RequestException
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import *
from .models import *

template_RequiredEncapped = "elemInstanceViewer.html"

class DataView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('auth_user_view')
    template_name = template_RequiredEncapped
    redirect_field_name = reverse_lazy('deauth_user_view')


    more_context = {
        "title_view": "Dashboard",
        "ClassInstance": str(__qualname__)
    }

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        view_context = super(DataView, self).get_context_data(**kwargs)
        view_context['user_instance_name'] = '%s %s %s' % (current_user.first_name, current_user.middle_name if current_user.middle_name is not None else '', current_user.last_name)
        view_context['user_branch'] = current_user.dept_residence

        view_context['ClassInstance'] = self.more_context['ClassInstance']
        return view_context

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

class DataAddition(LoginRequiredMixin, TemplateView):
    template_name = template_RequiredEncapped

    login_url = reverse_lazy('auth_user_view')
    next_page = login_url


class DataDeletion(LoginRequiredMixin, TemplateView):
    template_name = template_RequiredEncapped

    login_url = reverse_lazy('auth_user_view')
    next_page = login_url


class DataUpdate(LoginRequiredMixin, TemplateView):
    template_name = template_RequiredEncapped

    login_url = reverse_lazy('auth_user_view')
    next_page = login_url
