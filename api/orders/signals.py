from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Tracking
from datetime import timedelta


@receiver(post_save, sender=Order)
def create_tracking(sender, instance, created, **kwargs):
    if created:
        Tracking.objects.create(
            order=instance,
            tracking_number=instance.order_id,
            delivery_date=instance.date_created + timedelta(days=4),
            ship_to=instance.customer
        )


@receiver(post_save, sender=Order)
def update_tracking(sender, instance, created, **kwargs):
    if created is False:
        instance.tracking.save()
