from django.contrib import admin
from .models import employee, item, order, orderItem

admin.site.register(employee)
admin.site.register(item)
admin.site.register(order)
admin.site.register(orderItem)