from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from cart.models import Cart


def checkout(request):
    cart = Cart.objects.get(cart_id=request.session.session_key)
    print("cart", cart)
    # cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in the cart at the moment")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IVIJFIFvJ6ESH8psZDN5mmk1nPAbJAY6UE2LI79Ucjug9rEm24ibEfuBtg3Plgj2sYV7u9mexbUrLYh4uvMBzr900P3LWaRMq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
