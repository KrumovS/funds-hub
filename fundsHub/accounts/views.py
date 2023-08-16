from django.contrib.auth import views as auth_views, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from fundsHub.accounts.forms import FundsHubUserCreateForm, LoginForm, FundsHubUserEditForm, FundsHubUserDeleteForm
from fundsHub.accounts.models import FundsHubUser


@login_required
def show_profile_details(request, pk):
    user = FundsHubUser.objects.get(pk=pk)
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
            user = authenticate(username=request.user.username, password=password)
            if user and form.cleaned_data.get('confirm_deletion'):
                request.user.delete()
                return redirect('home')
            else:
                form.add_error('password', 'Incorrect password')
    else:
        form = FundsHubUserDeleteForm()

    return render(request, 'accounts/profile-delete-page.html', {'form': form})


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
    next_page = reverse_lazy('home')


class UserEditView(LoginRequiredMixin, views.UpdateView):
    model = FundsHubUser
    form_class = FundsHubUserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})
