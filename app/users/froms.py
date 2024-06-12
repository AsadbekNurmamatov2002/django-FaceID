from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'email','password1', 'password2']
        widget={"username": forms.TextInput(attrs={"class":"class-ps"})}
        widget={"email": forms.TextInput(attrs={"class":"class-ps"})}
        widget={"password1": forms.TextInput(attrs={"class":"class-ps"})}
        widget={"password2": forms.TextInput(attrs={"class":"class-ps"})}


    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    #     self