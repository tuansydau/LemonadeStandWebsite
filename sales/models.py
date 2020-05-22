from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


<<<<<<< HEAD
=======
# CR: model names should be in CameCase
>>>>>>> d79f559d365d23b28060e8b43b6918a4df3b5588
class item(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return self.name


class employee(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=7)
    commission = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return self.name


class orderItem(models.Model):
    product = models.ForeignKey(item, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name


class order(models.Model):
    orderID = models.AutoField(primary_key=True)
    items = models.ManyToManyField(item, blank=True)
    orderTime = models.DateTimeField(default=timezone.now)
    salesperson = models.ForeignKey(employee, on_delete=models.CASCADE)

    def total(self):
        orderTotal = sum([item.price for item in self.items.all()])
        return orderTotal

    def commissions(self):
        return (self.total() * self.salesperson.commission)

    # CR: I see that you decided to implement commission calculation in the report.
    # What happens if the employee was promoted? Should his commission recalculated retroactively?

    # CR: I am not sure that ManyToMany is the right relationship in this case...
    # CR: Please note that your migrations are not sync-ed with the models.
    # python manage.py makemigrations generated a new migration script...
    def __str__(self):
        return 'Order #{}'.format(self.orderID)
