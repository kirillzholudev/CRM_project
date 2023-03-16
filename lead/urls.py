from django.urls import path

from . import views


urlpatterns = [
	path("", views.leads_list, name='leads_list'),
	path("add-lead/", views.add_lead, name='add_lead'),
]

