from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Category, ProductSize
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .forms import ProductForm

# Create your views here.


def filter_products_by_category(request, category_id):
    category_name = Category.objects.get(pk=category_id).name
    products = Product.objects.filter(category__pk=category_id)
    print('Products', products)
    return render(request, 'products/products.html', {'products': products, 'category_name': category_name})  # noqa:501


def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'products/products.html', {'products': products, 'query': query})  # noqa:501


def all_products(request):

    products = Product.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sort_k = request.GET['sort']
            sort = sort_k
            if sort_k == 'name':
                sort_k = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_k = f'-{sort_k}'
            products = products.order_by(sort_k)

    curr_sort = f'{sort}_{direction}'

    context = {
        'products': products,
        'curr_sort': curr_sort
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product_sizes = list(ProductSize.objects.filter(product=product))
    context = {
        'product': product, 'sizes': product_sizes
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')  # noqa:501
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))