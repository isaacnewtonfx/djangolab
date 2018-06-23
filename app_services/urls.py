from django.urls import path
from . import views

urlpatterns = [
	path('contacts/<str:response_type>', views.contacts, name='contacts'),
	path('directions/', views.directions, name='directions'),
]