from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from fundsHub.accounts.forms import FundsHubUserCreateForm, LoginForm
from fundsHub.accounts.models import FundsHubUser


class UserRegisterView(views.CreateView):
    model = FundsHubUser
    form_class = FundsHubUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home')




