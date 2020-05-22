from django.contrib import admin
from .models import employee, item, order, orderItem

# CR: The admin could be more functional...
# Read more on how to customize the admin:
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/

admin.site.register(employee)
admin.site.register(item)
admin.site.register(order)
admin.site.register(orderItem)