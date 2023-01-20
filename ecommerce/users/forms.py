from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from  django import forms

class CustomUserCreationForm(UserCreationForm):

    def clean_password2(self):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')
      
      if len(password1) < 8:
            raise forms.ValidationError("Your password must contain at least 8 characters.")
      if password1.isdigit():
            raise forms.ValidationError("Your password can't be entirely numeric.")
      if  password1.isalnum():
            raise forms.ValidationError("Your password must contain letters , numbers and symbols.")
      if password1!=password2:
            raise forms.ValidationError("Your password doesn't match.")

      return password2
    class Meta:
        model = User
        fields = ('email','phone','first_name','last_name','phone','gender')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = fields = ('email','phone','first_name','last_name','phone','gender')
