from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm, UserCreationForm, LoginForm
from django.contrib import messages

def login(request):
    template_name = 'sales/login.html'
    form = LoginForm()
    return render(request, template_name, {'form':form})

def home(request):
    return render(request, 'sales/home.html')

def sales_form(request):
    form = OrderForm()
    template_name = 'sales/form.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            args = {'form':form, 'text':text}
            return render(request, self.template_name, {'form':form})

    #TWTif request.method == 'POST':
    #    form = OrderForm(request.POST)
    #    
    #    if form.is_valid():
    #        n = form.cleaned_data['OrderID']
    #        item = OrderItem(OrderID=n)

    return render(request, template_name, {'form':form})

def sales_report(request):
    return render(request, 'sales/report.html') 
