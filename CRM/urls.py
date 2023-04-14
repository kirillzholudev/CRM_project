from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path, include

from core.views import index
from userprofile.views import sign
from django.contrib.auth import views as auth_views

from django.urls import path
from userprofile.views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView


urlpatterns = [

    path('', index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('dasboard/leads/', include('lead.urls')),
    path('dashboard/clients/', include('client.urls')),
    path('accounts/sign-in/', sign, name='sign'),
    path('accounts/log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='userprofile/password_reset_form.html',
        email_template_name='userprofile/password_reset_email.html',
        subject_template_name='userprofile/password_reset_email.txt',
        success_url='/password_reset/done/'
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]



