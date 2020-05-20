from django import forms
from .models import item

class OrderForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=item.objects.all())
    
class UserCreationForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    passwordConfirm = forms.CharField(max_length=64, label="Confirm Password")

class LoginForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)