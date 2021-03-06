from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.all_products, name='products'),
    path('category/<category_id>', views.filter_products_by_category, name='product_category'),  # noqa:501
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # noqa:501
    path('<product_id>/', views.product_detail, name='product_detail'),
]
