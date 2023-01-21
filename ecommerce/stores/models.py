from users.models import User
from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=26,null=False)
    CATEGORIES=[('Guitar',' Acoustic Guitar'),('Guitar',' Electric Guitar'),
                ('Keyboard','Electric Keyboards'),
                ('Drums','Drum Set'),
                ('Flutes','Flute'),
                ('Steel','Violin'),
                ('Studio Equipments',' Equipments'),
                ('Pedals','Bass Guitars')]
    category=models.CharField(max_length=26,choices = CATEGORIES,null=False)
    image = models.ImageField(upload_to='uploads/products',null=True)
    price=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)
    product_info = models.TextField()
    brand = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    status=models.BooleanField(default=False)
    date_added=models.DateField(auto_now=True)

    @property
    def cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.total for item in cartitems])
        return total
    
    @property
    def cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total
    
    
    
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,null=False)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=False)
    quantity=models.IntegerField(default=0)

    @property
    def total(self):
        amount = self.product.price * self.quantity
        return amount

class ShippingLocation(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    cart = models.OneToOneField(Cart,on_delete=models.SET_NULL,null=True,blank=True)
    city=models.CharField(max_length=26,null=False)
    state=models.CharField(max_length=26,null=False)
    location=models.CharField(max_length=26,null=False)
    delivery_status=models.BooleanField(default=False)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        loc = self.location + ", " + self.city + ", " + self.state
        return loc
    
