from atexit import register
from django.urls import path
from .views import *

urlpatterns = [
    path('',getProducts,name='home'),
    path('login',LoginPage,name='login-page'),
    path('cart',viewCart,name='cart'),
    path('addToCart',createCartItem,name='addToCart'),
    path('checkout',checkout,name='checkout'),
    path('payment',payment,name='payment'),
    path('esewaverify',esewaverify,name='esewaverify'),
    path('register',register,name='register-page'),
    path('logout',LogoutPage,name='logout'),
]
