from django import forms
from .models import item


# CR: quantity of each item is missing
class OrderForm(forms.Form):
    items = forms.ModelMultipleChoiceField(queryset=item.objects.all())


# CR:don't you think that those forms belongs to the users app?

class UserCreationForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    passwordConfirm = forms.CharField(max_length=64, label="Confirm Password")

class LoginForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)