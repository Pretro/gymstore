from django.shortcuts import render


# Create your views here.


def shopping_cart(request):
    return render(request, 'cart/cart.html')