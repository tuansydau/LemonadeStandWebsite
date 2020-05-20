from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class item(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()

    def __str__(self):
        return self.name

class employee(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=7)
    commission = models.DecimalField(decimal_places=2, max_digits=3)
    
    def __str__(self):
        return self.name
    
class orderItem(models.Model):
    orderID = models.CharField(max_length=300)
    product = models.ForeignKey(item, on_delete=models.PROTECT, default="")
    quantity = models.IntegerField(default=1)

class order(models.Model):
    orderID = models.AutoField(primary_key=True)
    items = models.ManyToManyField(orderItem)
    orderTime = models.DateTimeField(default=timezone.now)
    
    # protected to ensure all orders are kept for accounting reasons
    salesperson = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return 'Order #{}'.format(self.orderID)
