from django.urls import path
from . import views

app_name = 'lab'
urlpatterns = [
	path('testit', views.testit, name='testit'),
	path('<int:pk>__<path:upn>__<path:acc_num>', views.UPNView.as_view(), name='upn'),
	
]