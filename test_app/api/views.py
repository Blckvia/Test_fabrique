from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import *

from .serializers import *


class MailingListViewSet(viewsets.ModelViewSet):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return MailingCountSerializer
        return MailingListSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['tag', 'code']


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer