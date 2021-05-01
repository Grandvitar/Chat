from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Messages
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
