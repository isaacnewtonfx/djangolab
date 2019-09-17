import json
import urllib.request

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from .serializers import ContactSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from app_contacts.models import Contact


# using core django API
def contacts(request, response_type="json"):
	if response_type == "json":
		# all_contacts = Contact.objects.values()
		# json_list = [entry for entry in all_contacts]
		# return HttpResponse(json.dumps(json_list), content_type='application/json')

		all_contacts = Contact.objects.all()
		jsondata = serializers.serialize("json", all_contacts)
		return HttpResponse(jsondata, content_type='application/json')
	else:
		all_contacts = Contact.objects.all()
		xmldata = serializers.serialize("xml", all_contacts)
		return HttpResponse(xmldata, content_type='application/xml')

# End using core django API


def directions(request):
	response = urllib.request.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=5.562437405336545,-0.26535860355439134&destination=5.558849480325817,-0.21557680424489564&key=AIzaSyBOnqS14BIBk3IZKjzrvBRF4ITDYyfUvtU")
	json = response.read()
	return HttpResponse(json, content_type='application/json')


# APIView Class defines the view behavior manually for the API,
# and also appropriate for use when there is some intermediate business
# logic to run before saving data
class ContactList(APIView):
	"""
    Retrieve all, and create new.
    """
	permission_classes = (permissions.DjangoModelPermissions,)
	serializer_class = ContactSerializer
	queryset = Contact.objects.none()

	# /contact_list
	def get(self, request, format=None):
		contacts = Contact.objects.all() #This can also be a Geodjango query operation
		serializer = ContactSerializer(contacts, many=True)
		return Response(serializer.data)

	# /contact_list
	def post(self, request, format=None):
		serializer = ContactSerializer(data=request.data, request=request)
		if serializer.is_valid():

			#serializer.validated_data['firstname'] = 'edited firstname'
			#print(serializer.validated_data)
			#print(request.data['lon'])
			#print(request.data['lat'])

			# Additional business logic code goes here

			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
	"""
	Retrieve, update or delete a contact.
	"""
	permission_classes = (permissions.DjangoModelPermissions,)
	serializer_class = ContactSerializer
	queryset = Contact.objects.none()

	def get_object(self, pk):
		try:
			return Contact.objects.get(pk=pk)
		except Contact.DoesNotExist:
			raise Http404

	# /contact_detail/id
	def get(self, request, pk, format=None):
		contact = self.get_object(pk)
		serializer = ContactSerializer(contact)
		return Response(serializer.data)

	# /contact_detail/id
	def put(self, request, pk, format=None):
		contact = self.get_object(pk)
		serializer = ContactSerializer(contact, data=request.data)
		if serializer.is_valid():

			# Additional business logic code goes here

			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# /contact_detail/id
	def delete(self, request, pk, format=None):
		contact = self.get_object(pk)

		# Additional business logic code goes here

		contact.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
	def get(self, request, format = None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	
	def post(self, request, format = None):
		pass





# ViewSets define the view behavior for (GET, POST, HEAD, OPTIONS) API, 
# and also appropriate for use when there is no intermediate business logic to run before saving data
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.DjangoModelPermissions,)

class ContactViewSet(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
	permission_classes = (permissions.DjangoModelPermissions,)