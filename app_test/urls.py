from django.urls import path
from . import views

app_name = 'test'
urlpatterns = [
	path('<int:pk>__<path:upn>__<path:acc_num>', views.UPNView.as_view(), name='upn'),
]