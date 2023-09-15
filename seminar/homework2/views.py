from django.shortcuts import render
from django.http import HttpResponse

from homework2.models import Product


def index(request):
    products = Product.objects.all()

    return HttpResponse(f'{products[2].price}')
