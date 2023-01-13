from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display= ['email','first_name','last_name','is_active']
    list_filter = ['gender','is_active','is_staff','is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','phone','gender')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name','last_name','gender','phone','is_staff', 'is_active')}
        ),
    )
    search_fields = ('email','first_name','last_name')
    ordering = ('email','first_name','last_name')

admin.site.register(User,CustomUserAdmin)