from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class post_form(forms.ModelForm):
    class Meta:


        model = Post
        fields = ['text', 'pic']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')
