from django import forms
from django.forms import ModelForm, TextInput, EmailInput,PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
       