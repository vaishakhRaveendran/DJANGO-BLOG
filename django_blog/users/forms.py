from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        #we specify the model with which the  form interact.When the form validates new user will be created.
        model= User
        #The fields we want to display
        fields = ['username','email','password1','password2']