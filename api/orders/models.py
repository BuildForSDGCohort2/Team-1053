from django.db import models
from api.inventory.models import Product
from api.accounts.models import Customer
from simple_history.models import HistoricalRecords


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('On Hold', 'On Hold'),
        ('Confirmed', 'Confirmed'),
        ('Canceled', 'Canceled'),
        ('Abandoned Cart', 'Abandoned Cart'),
    )
    code = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL
    )
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default='New'
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.order.price


class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    product_quantity = models.IntegerField(null=True)
    price = models.FloatField(default=0.00)
    order = models.ManyToManyField(Order)
    history = HistoricalRecords()

    def __str__(self):
        return self.product.name


class Tracking(models.Model):
    STATUS = (
        ('Packed', 'Packed'),
        ('Dispatched', 'Dispatched'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    tracking_number = models.CharField(max_length=200, null=True)
    order = models.ForeignKey(
        Order, null=True, on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default='Processing'
    )
    location = models.CharField(max_length=200, default='WareHouse')
    delivery_date = models.DateTimeField()
    ship_to = models.CharField(max_length=255, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.order.status} at {self.location}'
