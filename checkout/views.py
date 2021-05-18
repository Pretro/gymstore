from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents
from cart.models import Cart, CartItem
from products.models import Product

import stripe

def calculate_order_total(cart_items):
    total = 0
    for item in cart_items:
        product = item.product
        price = product.price
        total += price * item.quantity
    return total

def save_order_details(order, cart_items):
    for item in cart_items:
        print("order", order)
        try:
            product = item.product
            price = product.price
            order_line_item = OrderLineItem(
                order=order,
                product=product,
                quantity=item.quantity,
                lineitem_total=price * item.quantity,
            )
            order_line_item.save()
        except Product.DoesNotExist:
            raise



def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    try:
        cart = Cart.objects.get(cart_id=request.session.session_key)
        cart_items = list(CartItem.objects.filter(cart=cart))
    except:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

    if request.method == 'POST':
        print('HERE 1')
        total = calculate_order_total(cart_items)
        delivery = total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        form_data = {
            'billingName': request.POST['billingName'],
            'emailAddress': request.POST['emailAddress'],
            'phone': request.POST['phone'],
            'billingAdress1': request.POST['billingAdress1'],
            'billingCity': request.POST['billingCity'],
            'billingPostcode': request.POST['billingPostcode'],
            'billingCountry': request.POST['billingCountry'],
            'shippingName': request.POST['shippingName'],
            'shippingAddress1': request.POST['shippingAddress1'],
            'shippingCity': request.POST['shippingCity'],
            'shippingPostcode': request.POST['shippingPostcode'],
            'shippingCountry': request.POST['shippingCountry'],
            # 'grand_total': total + delivery,
            'total': total ,
            # 'delivery': delivery
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            try:
                order = order_form.save()
                order.grand_total = total + delivery
                order.delivery = delivery
                order.save()
                save_order_details(order, cart_items)

                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse('checkout_success', args=[order.order_number]))  # noqa:501
            except:
                messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                order.delete()
                return redirect(reverse('cart'))
        else:
            print('BAD FORM')
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        current_cart = cart_contents(request)
        total = current_cart['final_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.emailAddress}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

