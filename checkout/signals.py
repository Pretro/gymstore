from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

<<<<<<< HEAD
=======

>>>>>>> 3e14a58ecc09e090cbbc16ca2600c9c136a14ac3
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

<<<<<<< HEAD
@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
=======

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):

    instance.order.update_total()
>>>>>>> 3e14a58ecc09e090cbbc16ca2600c9c136a14ac3
