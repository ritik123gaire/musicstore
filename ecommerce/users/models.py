from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,null=False)
    first_name=models.CharField(max_length=26,null=False)
    last_name=models.CharField(max_length=26,null=False)
    phone=models.CharField(max_length=10,null=False)

    GENDER = [('Male','Male'),('Female','Female'),('Other','Other')]
    gender=models.CharField(max_length=6,choices=GENDER,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined=models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone','gender']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
