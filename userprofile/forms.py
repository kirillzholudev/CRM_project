


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput())
    password1 = forms.CharField(max_length=254, required=True, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=254, required=True, label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')