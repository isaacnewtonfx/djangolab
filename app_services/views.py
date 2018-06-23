from django.core import serializers
from django.http import HttpResponse
from app_contacts.models import Contact
import json,urllib


def contacts(request,response_type = "json"):
	if response_type == "json":
		all_contacts = Contact.objects.values()
		json_list = [entry for entry in all_contacts]	
		return HttpResponse(json.dumps(json_list), content_type='application/json')
	else:
		all_contacts = Contact.objects.all()
		xmldata = serializers.serialize("xml", all_contacts)
		return HttpResponse(xmldata,content_type='application/xml')


def directions(request):
	raw = urllib.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=5.562437405336545,-0.26535860355439134&destination=5.558849480325817,-0.21557680424489564&key=AIzaSyBOnqS14BIBk3IZKjzrvBRF4ITDYyfUvtU")
	js = raw.readlines()
	return HttpResponse(js)