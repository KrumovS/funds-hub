from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views

from fundsHub.accounts.forms import FundsHubUserCreateForm, LoginForm, FundsHubUserEditForm
from fundsHub.accounts.models import FundsHubUser


def show_profile_details(request, pk):
    user = FundsHubUser.objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, template_name='accounts/profile-details-page.html', context=context)


def delete_profile(request, pk):
    user = FundsHubUser.objects.get(pk=pk)
    context = {
        "user": user,
    }
    return render(request, template_name='accounts/profile-delete-page.html', context=context)


class UserRegisterView(views.CreateView):
    model = FundsHubUser
    form_class = FundsHubUserCreateForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserEditView(views.UpdateView):
    model = FundsHubUser
    form_class = FundsHubUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

