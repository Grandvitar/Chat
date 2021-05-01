from rest_framework import viewsets
from rest_framework.response import Response

from django.contrib.auth.models import User

from .models import Messages
from .serializers import MessagesSerializer, UserSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.decorators import action


class MessagesSendViewSet(viewsets.ModelViewSet):
    serializer_class = MessagesSerializer
    queryset = Messages.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer
    filterset_fields = ['target', 'author']

    @action(methods=['get'], detail=True)
    def all_from_me(self, request):
        user = self.request.user
        serializer = MessagesSerializer(Messages.objects.filter(author=user), many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def all_for_me(self, request):
        user = self.request.user
        return Response(Messages.objects.filter(target=user))

    @action(methods=['get'], detail=True)
    def from_me_to(self, request):
        user = self.request.user
        target = self.request.query_params.get('user')
        return Response(Messages.objects.filter(author=user, target=target))

    @action(methods=['get'], detail=True)
    def for_me_from(self, request):
        user = self.request.user
        author = self.request.query_params.get('author')
        return Response(Messages.objects.filter(target=user, author=author))


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer






