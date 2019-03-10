from rest_framework import serializers

from accounts.models import Automobiliste
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class AutomobilisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Automobiliste
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}







