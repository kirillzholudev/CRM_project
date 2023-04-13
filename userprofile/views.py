from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages


def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request, user)

                return redirect('/dashboard/')
            else:
                messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/sign.html', {'form': form})