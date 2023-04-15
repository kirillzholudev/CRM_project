


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={'class': 'form-field', 'autocorrect': 'off', 'autofocus': 'off', 'spellcheck': 'off', 'autocapitalize': 'off', 'value': '', 'autocomplete': 'username', 'inputmode': 'email'}))
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-field', 'autocorrect': 'off', 'autofocus': 'off', 'spellcheck': 'off', 'autocapitalize': 'off', 'value': '', 'autocomplete': 'username', 'inputmode': 'username'}))
    password1 = forms.CharField(max_length=254, required=True, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-field', 'autocomplete': 'password'}))
    password2 = forms.CharField(max_length=254, required=True, label='Confirm Password', widget=forms.PasswordInput({'class': 'form-field', 'autocomplete': 'password'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')