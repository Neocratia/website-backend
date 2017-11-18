from django_base.users.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, ActionSerializer
from .models import Contact


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ActionSerializer
    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
