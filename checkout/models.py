from django.db import models
from products.models import Product
from django.db.models import Sum
from django.conf import settings
import uuid


# Model: Order
class Order(models.Model):
    order_number = models.CharField(max_length=35, null=False, editable=False)
    emailAddress = models.EmailField(max_length=250, blank=True,verbose_name='Email Adress')  # noqa:501
    phone = models.CharField(max_length=15, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAdress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=250, blank=True)
    billingCountry = models.CharField(max_length=250, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostcode = models.CharField(max_length=250, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')  # noqa:501
    order_total = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)


def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()


def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']  # noqa:501
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100  # noqa:501
        else:
            self.delivery_cost = 0
        self.total = self.order_total + self.delivery_cost
        self.save()


class Meta:
    db_table = 'Order'
    ordering = ['-created']


def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Price')  # noqa:501
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self._price

    def __str__(self):
        return self.product


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'