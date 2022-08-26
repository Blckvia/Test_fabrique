from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MailingListViewSet, ClientViewSet, MessageViewSet

router = DefaultRouter()
router.register('Mailing', MailingListViewSet)
router.register('Client', ClientViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]