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

# main_template view...

class DataView(PermissionRequiredMixin, TemplateView):
    pass

class UserAuthView(LoginView):
    pass
    # template_name = template_view
    # form_class = UserAuthForm
    # success_url = reverse_lazy('dashboard_user_view')
    # redirect_authenticated_user = True

    # more_context = {
    #     "title_view": "User Login",
    #     "ClassInstance": str(__qualname__),
    # }


    # def get_context_data(self, **kwargs):
    #     view_context = super(AuthUserView, self).get_context_data(**kwargs)
    #     view_context['title_view'] = self.more_context['title_view']
    #     view_context['ClassInstance'] = self.more_context['ClassInstance']

    #     return view_context

    # def get_success_url(self):
    #     return self.success_url


class UserDeauthView(LoginRequiredMixin, LogoutView):
    pass
    # template_name = template_view

    # login_url = reverse_lazy('auth_user_view')
    # next_page = login_url

    # def dispatch(self, request):
    #      if request.user.is_authenticated:
    #         messages.success(self.request, "UserLoggedOut")
    #     return super(DeauthUserView, self).dispatch(request)

    # def handle_no_permission(self):
    #     messages.error(self.request, "UserAlreadyLoggedOut")
    #     return super(DeauthUserView ,self).handle_no_permission()

class DataAddition(PermissionRequiredMixin, TemplateView):
        # permission_required = 'SCControlSystem.classroom_action_log_viewable'
    pass

class DataDeletion(PermissionRequiredMixin, TemplateView):
        # permission_required = 'SCControlSystem.classroom_action_log_viewable'
    pass

class DataUpdate(PermissionRequiredMixin, TemplateView):
        # permission_required = 'SCControlSystem.classroom_action_log_viewable'
    pass
