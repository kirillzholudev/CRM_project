from django.urls import path

from . import views


urlpatterns = [
	path("", views.leads_list, name='leads_list'),
	path('<int:pk>/', views.leads_detail, name='leads_detail'),
	path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
	path('<int:pk>/edit/', views.edit_lead, name='edit_lead'),
	path('<int:pk>/convert/', views.convert_to_client, name='leads_convert'),
	path("add-lead/", views.add_lead, name='add_lead'),
]

