from django.shortcuts import render
from django.core.serializers import serialize
from .models import WorldBorder,places
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
import json,urllib


class WorldGeojson(View):
	
	def get(self, request):

		geojson = serialize('geojson', WorldBorder.objects.all()[:1],
		          geometry_field='mpoly',fields=('name','area',))

		data = {'geojson' : json.loads(geojson), 'error' : False}
		return JsonResponse(data)
