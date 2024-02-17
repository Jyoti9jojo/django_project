from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def index(request):
    print(request.method)
    return HttpResponse("<h1><i>This is the index page! Hello world</i></h1>")


def products(request):
    products = Products.objects.all()
    context = { 
        "products": products, 
        "product_count": len(products)
    }
    return render(request, 'products.html', context=context)


@csrf_exempt
def user_registration(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            message = "Incorrect password"
        else:
            message = "Correct password"
        
        existing_user = User.objects.filter(username=username).first()
        print(existing_user)
        if existing_user:
            message = 'this user already exists'
        else:
            # user = User(username=username, email=email, password=password)
            user = User.objects.create_user(username=username, email=email, password=password)
            products = Products.objects.create()
            user.save()
            print(username, email, password, confirm_password)
        context = {"message": message}
    return render(request, 'user_registration.html', context)


def user_login(request):
    pass