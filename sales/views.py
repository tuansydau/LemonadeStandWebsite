from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import OrderForm, UserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import orderItem, item, employee, order


def login(request):
    template_name = 'sales/login.html'
    form = LoginForm()
    return render(request, template_name, {'form': form})


def home(request):
    return render(request, 'sales/home.html')


@login_required
def sales_form(request):
    form = OrderForm()
    template_name = 'sales/form.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        items = request.POST['items']
        salesperson = request.POST['salesperson']
        orderInfo = order(items=items, salesperson=salesperson)

        form = OrderForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            args = {'form': form, 'text': text}
            return render(request, self.template_name, {'form': form})

    return render(request, template_name, {'form': form})


def submit_sales_form(request):
    print("form is submitted")
    items = request.POST['items']
    salesperson = request.POST['salesperson']

    salesperson = employee.objects.get(id=salesperson)

    def maxID(order):
        highestID = 0
        for instance in order.objects.all():
            if instance.orderID > highestID:
                highestID = instance.orderID

        return highestID

    orderInfo = order(orderID=maxID(order)+1, salesperson=salesperson)
    orderInfo.save()

    for item in items:
        orderInfo.items.add(item)

    orderInfo.save()

    return render(request, "sales/form.html", {'form': OrderForm()})

# @login_required
# def sales_form(request):
#     items = list(item.objects.all())
#     return render(request, 'sales/form.html', {'items': items})


def view(request):
    Order = order.objects.filter(salesperson__name="Larry Long", orderTime__range=["2011-01-11", "2020-05-26"])

    def all_orders_total(self):
        allOrdersTotal = 0.00
        allOrdersTotal = sum([instance.total for instance in self.Order.all()])
        return allOrdersTotal

    context = {"Order": Order}
    template = "sales/view.html"
    return render(request, template, context)


# def add_to_order(request, slug):
#     order = Order.objects.all()[0]
#     try:
#         product = item.objects.get(slug=slug)
#     except item.DoesNotExist:
#         pass
#     except:
#         pass
#     if not product in order.products.all():
#         order.item.add(product)
#     else:
#         order.products.remove(product)
#     return HttpResponseRedirect(reverse('sales-view'))


@login_required
def sales_report(request):
    return render(request, 'sales/report.html')
