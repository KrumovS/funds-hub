from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from fundsHub.accounts.models import FundsHubUser


class FundsHubUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = FundsHubUser
        fields = ('username', 'email')


class FundsHubUserEditForm(forms.ModelForm):
    class Meta():
        model = FundsHubUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')
        exclude = ('password',)
        labels = {'username': 'Username',
                  'first_name': 'First Name:',
                  'last_name': 'Last Name',
                  'email': 'Email',
                  'profile_picture': 'Image:',
                  }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, "placeholder": "Username", 'class': 'form-control'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "placeholder": "Password", 'class': 'form-control'})
    )
