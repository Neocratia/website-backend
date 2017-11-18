from django_base.users.models import User
from rest_framework import status, viewsets
from .serializers import UserSerializer, ContactSerializer
from .models import Contact
from rest_framework.response import Response
from django_slack import slack_message
from django.conf import settings
import json
import requests

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        requests.post(
            settings.SLACK_WEBHOOK_URL,
            data=json.dumps(
                {"text":"Somebody wants to join Neocratia\nEmail: {}\nInterest: {}".format(serializer.data['email'],', '.join(serializer.data['interests']))}),
            headers={'content-type':'application/json'}
        )

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)
