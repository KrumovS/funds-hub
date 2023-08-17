from django.contrib.auth import authenticate, views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from fundsHub.accounts.forms import (
    FundsHubUserCreationForm, FundsHubLoginForm,
    FundsHubUserEditForm, FundsHubUserDeleteForm
)
from fundsHub.accounts.models import FundsHubUser


@login_required
def show_profile_details(request, pk):
    user = get_object_or_404(FundsHubUser, pk=pk)
    context = {
        "user": user,
    }
    return render(request, template_name='accounts/profile-details-page.html', context=context)


@login_required
def delete_profile(request, pk):
    if request.method == 'POST':
        form = FundsHubUserDeleteForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            auth_user = authenticate(username=request.user.username, password=password)
            if not auth_user:
                form.add_error(field='password', error='Incorrect password')
            elif form.cleaned_data.get('confirm_deletion'):
                request.user.delete()
                return redirect('home')
    else:
        form = FundsHubUserDeleteForm()

    context = {
        "form": form,
    }

    return render(request, template_name='accounts/profile-delete-page.html', context=context)


class UserRegisterView(views.CreateView):
    model = FundsHubUser
    form_class = FundsHubUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class UserLoginView(auth_views.LoginView):
    form_class = FundsHubLoginForm
    template_name = 'accounts/login-page.html'
    next_page = reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home')


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = FundsHubUser
    form_class = FundsHubUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})
