from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello world')


def newproduct(request):
    return HttpResponse('This is a new product')
