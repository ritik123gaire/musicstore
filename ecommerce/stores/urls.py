from atexit import register
from django.urls import path
from .views import *

urlpatterns = [
    path('',getProducts,name='home'),
    path('login',LoginPage,name='login-page'),
    path('cart',viewCart,name='cart'),
    path('addToCart',createCartItem,name='addToCart'),
    path('checkout',checkout,name='checkout'),
    path('category/',category,name='category'),
    path('search/', search,name='search'),
    path('payment',payment,name='payment'),
    path('esewaverify',esewaverify,name='esewaverify'),
    path('register',register,name='register-page'),
    path('logout',LogoutPage,name='logout'),
    path('products_json',products_json,name='products_json'),
    path('product/<int:pk>/',productdetails,name='product'),
    
    
]
