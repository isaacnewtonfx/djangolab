from rest_framework import serializers
from app_contacts.models import Contact
from django.contrib.auth.models import User


# Serializers define the API representation.
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('__all__')

    # Constructor ( Override default constructor )
    def __init__(self, *args, **kwargs):

        # pop out the request object and add it as an instance attribute
        self.request = kwargs.pop('request', None)

        # now call the parent constructor
        super(ContactSerializer, self).__init__(*args, **kwargs)


    def validate(self, data):
        """
        Do any custom validations for any field here.
        """
        # if 'lon' not in self.request.data:
        #     raise serializers.ValidationError("Longitude not found")
        # elif 'lon' not in self.request.data:
        #     raise serializers.ValidationError("Latitude not found")
        return data
        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        #depth = 1 #used to go one step deep on the related fields