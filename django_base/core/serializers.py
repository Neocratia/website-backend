from django_base.users.models import User
from .models import Contact
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'name', 'username', 'email', 'is_staff')

class ActionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('email','interests',)
