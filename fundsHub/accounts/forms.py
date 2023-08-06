from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from fundsHub.accounts.models import FundsHubUser


class FundsHubUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = FundsHubUser
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username"}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password"})
    )
