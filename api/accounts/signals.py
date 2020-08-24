from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .models import User, Customer


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get_or_create(name='customer')
        print(group[0])
        # instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username
        )
        print('customer created')


@receiver(post_save, sender=User)
def update_customer(sender, instance, created, **kwargs):
    if created is False:
        instance.customer.save()
        print('customer updated')
