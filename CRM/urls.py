from django.contrib import admin
from django.urls import path

from core.views import index
from userprofile.views import sign

urlpatterns = [
    path('', index, name='index'),
    path('sign-up/', sign, name='sign'),
    path('admin/', admin.site.urls),

]
