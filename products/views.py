from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'list_of_products.html', {'products': products})
