from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите имя",
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите логин",
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите возраст",
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': "example@ex.com",
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Введите пароль",
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': "Повторите пароль",
    }))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'age', 'email', 'password1', 'password2')