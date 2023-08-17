from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from fundsHub.accounts.models import FundsHubUser


class FundsHubUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = FundsHubUser
        fields = ('username', 'email')


class FundsHubUserEditForm(forms.ModelForm):
    class Meta:
        model = FundsHubUser
        fields = ('first_name', 'last_name', 'email', 'profile_picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
        }


class FundsHubUserDeleteForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirm Password'
    )
    confirm_deletion = forms.BooleanField(
        initial=False,
        required=True,
        label='I understand that deleting my account is irreversible.'
    )


class FundsHubLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "placeholder": "Username",
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "placeholder": "Password",
            'class': 'form-control'
        })
    )
