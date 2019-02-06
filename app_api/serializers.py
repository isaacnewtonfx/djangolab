from rest_framework import serializers
from app_contacts.models import Contact
from django.contrib.auth.models import User


# Serializers define the API representation.
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        #depth = 1 #used to go one step deep on the related fields