from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def index(request):
    print(request.method)
    return HttpResponse("<h1><i>This is the index page! Hello world</i></h1>")


def products(request):
    products = Products.objects.all()
    print(products)
    return HttpResponse(products)
