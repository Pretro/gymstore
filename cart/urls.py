from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_cart, name='cart'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name='cart_detail'),
]
