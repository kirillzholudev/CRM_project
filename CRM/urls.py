from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from core.views import index
from userprofile.views import sign

urlpatterns = [
    path('', index, name='index'),
    path('sign-up/', sign, name='sign'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),

]


