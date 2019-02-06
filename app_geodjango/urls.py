from django.urls import include,path
from . import views

app_name = 'geodjango'
urlpatterns = [
	path('worldgeojson/', views.WorldGeojson.as_view(), name='geojson'),
]