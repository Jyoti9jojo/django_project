from django.urls import path
from .views import (index, products, user_login, user_registration)

urlpatterns = [
    path('index/', index, name="index"),
    path('products/', products, name="products"),
    path('user_registration/', user_registration, name="user_registration"),
    path('user_login/', user_login, name="user_login"),
]
