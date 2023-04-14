from django.contrib import messages


from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm



def sign(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/dashboard/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = SignUpForm()

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