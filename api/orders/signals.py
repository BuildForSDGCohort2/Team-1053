from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Tracking

locations = {
        'New': 'WareHouse',
        'On Hold': 'Waiting approval at WareHouse',
        'Confirmed': 'Is being Packed',
        'Canceled': 'This order is no longer available',
        'Abandoned Cart': 'Returned to warehouse',
        'Packed': 'Ready for transit',
        'Dispatched': 'Order has left our premises for delivery',
        'Out for delivery': 'Order in transit and will be delivered',
        'Delivered': 'Order delivered to the customer',
    }


@receiver(post_save, sender=Order)
def create_tracking(sender, instance, created, **kwargs):
    if created:
        Tracking.objects.create(
            order_id=instance.order_id,
            event=instance.status,
            ship_to=instance.customer,
            location=locations[instance.status],
            delivery_date=instance.expected_delivery,
        )


@receiver(post_save, sender=Order)
def update_tracking(sender, instance, created, **kwargs):
    if not created:
        Tracking.objects.create(
            order_id=instance.order_id,
            event=instance.status,
            ship_to=instance.customer,
            location=locations[instance.status],
            delivery_date=instance.expected_delivery,
        )
