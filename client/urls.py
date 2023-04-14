from django.urls import path

from . import views

urlpatterns = [
	path("", views.client_list, name="clients_list"),
    path('create/', views.create_client, name='create_client'),
    path('<int:pk>/', views.view_client, name='view_client'),
    path('<int:pk>/update/', views.update_client, name='update_client'),
    path('<int:pk>/delete/', views.delete_client, name='delete_client'),
]