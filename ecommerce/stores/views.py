from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import *
from django.conf import settings
from users.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
import requests
import random

def getProducts(request):
    product = Product.objects.all().order_by('-date_added')
    context = {
        "products" : product
    }
    return render(request,"pages/home.html",context)


@login_required(login_url='login-page')
def viewCart(request):
    if request.user.is_authenticated:
        customer = User.objects.get(id= request.user.id)
        cart, created = Cart.objects.get_or_create(user = customer,status = False)
        items = cart.cartitem_set.all()
    else:
        items=[]
        cart ={'cart_total':0, 'cart_items':0}
    context={
        "items":items,
        "cart":cart
    }
    return render(request,"pages/cart.html",context)

def createCartItem(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        customer = User.objects.get(id= request.user.id)
        product = Product.objects.get(id = productId)
        cart, created = Cart.objects.get_or_create(user = customer,status = False)

        cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if action == 'add':
            cartItem.quantity = (cartItem.quantity + 1)
        elif action == 'remove':
            cartItem.quantity = (cartItem.quantity - 1)

        cartItem.save()

        if cartItem.quantity <= 0:
            cartItem.delete()
    else:
        return JsonResponse({'status':500})

    return JsonResponse({'status': 200})


@login_required(login_url='login-page')
def checkout(request):
    user = User.objects.get(id = request.user.id)
    cart,created = Cart.objects.get_or_create(user= user, status = False)
    if request.method == 'POST':
        city_data=request.POST['city']
        location_data=request.POST['location']
        state_data=request.POST['state']
        cart_data=request.POST['cart']
        cart_instance = Cart.objects.get(id=cart_data)
        if city_data and location_data and state_data and cart_instance:
            shipping_location, created = ShippingLocation.objects.update_or_create(
                cart=cart_instance,
                defaults={
                    'user': user,
                    'city': city_data, 
                    'location': location_data, 
                    'state': state_data,
                    'delivery_status': False
                }
            )
            return redirect('payment')
        if not city_data or not location_data or not state_data or not cart_instance:
            messages.error(request, 'Please fill out all fields')
            return redirect('checkout')

    return render(request,"pages/checkout.html",{"cart":cart})





@login_required(login_url='login-page')
def payment(request):
    user = User.objects.get(id = request.user.id)
    cart,created = Cart.objects.get_or_create(user= user, status = False)

    return render(request,"pages/payment.html",{"cart":cart})

def esewaverify(request):
        import xml.etree.ElementTree as ET
        oid = request.GET.get("oid")
        amt = request.GET.get("amt")
        refId = request.GET.get("refId")

        url = "https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)
        root = ET.fromstring(resp.content)
        status = root[0].text.strip()

        order_id = oid.split("_")[1]
        order_obj = Cart.objects.get(id=order_id)
        if status == "Success":
            order_obj.status = True
            order_obj.save()
            return redirect("/")
        else:
            return redirect("/payment/")



def LoginPage(request):
    context = {}
    next = request.GET.get('next')
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            user = authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                if next:
                    return redirect(next)
                else:
                    return redirect('home')
            else:
                context['message'] = 'Incorrect Email or Password'
    return render(request,"pages/login.html",context)
    
def register(request):
    forms = CustomUserCreationForm()

    if request.method == 'POST':
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('login-page')
        else:
            context = {
                "form" :forms
            }
            return render(request,"pages/register.html",context)

    context = {
        "form" :forms
    }
    return render(request,"pages/register.html",context)
   

def LogoutPage(request):
    logout(request)
    return redirect('login-page')

def category(request):
    product = Product.objects.all()
    context = {
        "products" : product
    }
    return render(request, 'pages/category.html',context)


def category_view(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'pages/category.html', {'products': products, 'category': category})

def search(request):
    query = request.GET.get('query', '')
    if not query:
        return render(request, 'pages/search_results.html', {'products': []})
    products = Product.objects.filter(name__icontains=query)
    return render(request, 'pages/search_results.html', {'products': products})

def productdetails(request,pk):
    product = Product.objects.get(id=pk)
    context = {
        "product" : product
    }
    return render(request, 'pages/product.html',context)

# def products_json(request):
#     products = Product.objects.all()
#     products_json = json.dumps(list(products.values()),default=str)
#     return JsonResponse(json.loads(products_json), safe=False)

def products_json(request):
    products = Product.objects.all()
    products_json = json.dumps(list(products.values()),default=str)
    return JsonResponse(json.loads(products_json),safe=False)


