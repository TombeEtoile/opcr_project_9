from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Nom', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Nom', help_text='Entrez votre pseudo', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Confirmez votre mot de passe', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='Nom', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')
