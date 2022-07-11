from collections import UserDict
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DatosFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    

class UserRegisterForm(UserCreationForm):
   
    username= forms.CharField()
    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    last_name= forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    
    
    email=forms.EmailField(label="Modificar E-mail")
    password1= forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2: forms.CharField(label= 'Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} 