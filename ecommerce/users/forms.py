from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','phone','first_name','last_name','phone','gender')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = fields = ('email','phone','first_name','last_name','phone','gender')
