from django.urls import path
from . import views

urlpatterns = [
	path('all/<str:response_type>', views.contacts, name='contacts'),
	path('directions/', views.directions, name='directions'),
	path('contact_list/', views.ContactList.as_view()),
	path('contact_detail/<int:pk>', views.ContactDetail.as_view()),
	path('user_list/', views.UserList.as_view())
]