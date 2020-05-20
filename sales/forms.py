from django import forms
from .models import item, employee


class OrderForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=item.objects.all())
    salesperson = forms.ModelChoiceField(queryset=employee.objects.all())

class UserCreationForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    passwordConfirm = forms.CharField(max_length=64, label="Confirm Password")

class LoginForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)