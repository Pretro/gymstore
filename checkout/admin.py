from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('lineitem_total')


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'created',
                       'delivery_cost', 'order_total',
                       'total',)

    fields = ('order_number', 'emailAddress', 'created',
              'billingName', 'billingAdress1', 'billingCity',
              'billingPostcode', 'billingCountry', 'shippingName',
              'shippingAddress1', 'shippingCity', 'shippingPostcode',
              'shippingCountry', 'total', 'order_total', 'delivery_cost',)

    listdisplay = ('order_number', 'created', 'billingName',
                   'order_total', 'delivery_cost', 'total',)

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
