from django import forms

class OrderForm(forms.Form):
    post = forms.CharField(max_length=200)
    email = forms.EmailField(label = "E-Mail")
    check = forms.BooleanField(required=False)

class UserCreationForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    passwordConfirm = forms.CharField(max_length=64, label="Confirm Password")

class LoginForm(forms.Form):
    userID = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)