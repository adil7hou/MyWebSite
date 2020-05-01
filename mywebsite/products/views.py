from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html')


def newproduct(request):
    return HttpResponse('This is a new product')
