from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    # instance.order.total()
    print('After save ', instance)


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    print('delete signal received')
<<<<<<< HEAD
    instance.order.total()
=======
    # instance.order.total()
    print('After Delete ', instance)
>>>>>>> 561572997eb5b09a5cee9d4a6f0efbeeff5f5dd2
