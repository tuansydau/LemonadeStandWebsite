from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sales-home'),
    path('sales/form/', views.sales_form, name='sales-form'),
    path('sales/report/', views.sales_report, name='sales-report'),
    path('submit_sales_form/', views.submit_sales_form, name='sales-form-submit')
]
