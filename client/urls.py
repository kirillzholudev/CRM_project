from django.urls import path

from . import views

urlpatterns = [
	path("", views.clients_list, name="clients_list"),
	path("<int:pk>/", views.clients_detail, name="clients_detail"),
]