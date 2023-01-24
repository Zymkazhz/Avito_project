from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label='Никнейм')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=30)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    number_phone = forms.CharField(label='Номер телефона', max_length=12)
    image = forms.ImageField(label='Аватар')

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'number_phone']
