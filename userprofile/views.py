from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages


from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

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


class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'userprofile/password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_email.txt'
    success_url = reverse_lazy('password_reset_done')


class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'userprofile/password_reset_done.html'


class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'userprofile/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'userprofile/password_reset_complete.html'