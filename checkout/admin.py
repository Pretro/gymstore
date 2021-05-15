from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
<<<<<<< HEAD
    readonly_fields = ('lineitem_total',)
=======
    readonly_fields = ('lineitem_total')
>>>>>>> 3e14a58ecc09e090cbbc16ca2600c9c136a14ac3


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'created',
                       'delivery_cost', 'grand_total',
                       'total')

    fields = ('order_number', 'created', 'billingName', 
              'emailAddress', 'billingAdress1', 'billingCity',
              'billingPostcode', 'billingCountry', 'shippingName',
              'shippingAddress1', 'shippingCity', 'shippingPostcode',
              'shippingCountry', 'total', 'grand_total', 'delivery_cost')

    listdisplay = ('order_number', 'created', 'billingName',
                   '_total', 'delivery_cost', 'total',)

    ordering = ('-created',)


admin.site.register(Order, OrderAdmin)
