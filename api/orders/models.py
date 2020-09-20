from django.db import models
from api.inventory.models import Product
from api.accounts.models import Customer
from simple_history.models import HistoricalRecords


class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    history = HistoricalRecords()
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        """Return string representation of the OrderItem object"""

        return str(self.product.name)


class Order(models.Model):
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
    order_items = models.ManyToManyField(OrderItem)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    payment_option = models.CharField(
        max_length=200, null=True,
        choices=PAYMENT_OPTIONS,
        default='Cash On Delivery'
    )
    history = HistoricalRecords()

    def __str__(self):
        """Return string representation of the order object"""

        return f'{self.order_id}'


class Tracking(models.Model):
    STATUS = (
        ('Packed', 'Packed'),
        ('Dispatched', 'Dispatched'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    tracking_number = models.CharField(max_length=200, null=True)
    order = models.OneToOneField(
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
        """Return string representation of the Tracking object"""

        return f'{self.order.status} at {self.location}'
