from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from .views import MessagesSendViewSet, MessagesViewSet, UserViewSet

router = DefaultRouter()
router.register(r'messages/send', MessagesSendViewSet, basename='messages_send')
router.register(r'messages', MessagesViewSet, basename='messages-watch')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
