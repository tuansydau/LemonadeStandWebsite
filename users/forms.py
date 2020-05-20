from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    name = forms.CharField(required=False, label="Full Name (optional)")

    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2']