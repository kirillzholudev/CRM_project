from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Userprofile


def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user_profile = Userprofile.objects.create(user=user)

            # Authenticate and log in the user.
            user = authenticate(
                username=user.username,
                password=request.POST['password1']
            )
            login(request, user)

            # Redirect to the dashboard.
            return redirect('/dashboard/')

    else:
        form = UserCreationForm()

    return render(request, 'userprofile/sign.html', {'form': form})