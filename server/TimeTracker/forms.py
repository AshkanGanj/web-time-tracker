from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'password1','password2']


class Login(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
