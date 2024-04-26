from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products/list_of_products.html', {'products': products})


def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/show_product.html', {"product": product})
