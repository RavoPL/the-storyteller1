from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    # Gives the form an e-mail field
    email = forms.EmailField()
    # Specifies the user model and makes an ordered list of fields to display
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']