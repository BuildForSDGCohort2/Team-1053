from datetime import datetime, timedelta

from api.accounts.models import Customer
from api.inventory.models import Product
from django.db import models


class Order(models.Model):
    DELIVERY_DATE = datetime.now() + timedelta(days=4)
    STATUS = (
        ('New', 'New'),
        ('On Hold', 'On Hold'),
        ('Confirmed', 'Confirmed'),
        ('Canceled', 'Canceled'),
        ('Abandoned Cart', 'Abandoned Cart'),
        ('Packed', 'Packed'),
        ('Dispatched', 'Dispatched'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    PAYMENT_OPTIONS = (
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Paypal', 'Paypal'),
        ('Credit Card', 'Credit Card'),
    )
    order_id = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL
    )
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default='New'
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    payment_option = models.CharField(
        max_length=200, null=True,
        choices=PAYMENT_OPTIONS,
        default='Cash On Delivery'
    )
    expected_delivery = models.DateTimeField(default=DELIVERY_DATE, null=True)

    def __str__(self):
        """Return string representation of the order object"""

        return f'{self.order_id}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, null=True, unique=False, on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, default=0)
    cost = models.IntegerField(null=False, default=0)

    def __str__(self):
        """Return string representation of the OrderItem object"""

        return str(self.cost)


class Tracking(models.Model):
    event = models.CharField(max_length=255, null=True)
    event_date = models.DateTimeField(auto_now_add=True, null=True)
    order_id = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=200, default='WareHouse')
    delivery_date = models.DateTimeField()
    ship_to = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Return string representation of the Tracking object"""

        return f'{self.location}'
