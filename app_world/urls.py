from django.urls import include,path
from . import views

app_name = 'world'
urlpatterns = [
	path('geojson/', views.WorldGeojson.as_view(), name='geojson'),
]