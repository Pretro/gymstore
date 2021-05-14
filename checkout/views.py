from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents
from cart.models import Cart, CartItem

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = Cart.objects.get(cart_id=request.session.session_key)
    cart_items = list(CartItem.objects.filter(cart=cart))
    if not cart:
        messages.error(request, "There is nothing in the cart at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['final_total']
    stripe_total = round(total)
    stripe.api_key = stripe_secret_key
    print('total', stripe_total)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IVIJFIFvJ6ESH8psZDN5mmk1nPAbJAY6UE2LI79Ucjug9rEm24ibEfuBtg3Plgj2sYV7u9mexbUrLYh4uvMBzr900P3LWaRMq',  # noqa:501
        'client_secret': 'test client secret',
        'cart_items': cart_items
    }

    return render(request, template, context)