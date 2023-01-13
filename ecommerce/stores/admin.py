from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['name','price']
    list_filter=['category']
    search_fields=['category','name']

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ['user','cart_total','cart_items','status','date_added']
    list_filter=['user']

class CartItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ['product','quantity','total']

admin.site.register(Product,ProductAdmin)
admin.site.register(CartItem,CartItemAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(ShippingLocation)
