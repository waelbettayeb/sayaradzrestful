from rest_framework import serializers

from accounts.models import Automobiliste
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('password', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class AutomobilisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Automobiliste
        fields = ('email')


class FabriquantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabriquant
        fields = ('email','password','nom','prenom','adresse','tel','marque')
        extra_kwargs = {'password' : {'write_only' : True}}


class UtilisateurFabrquantSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.UtilisateurFabriquant
        fields = ('email','password','nom','prenom','tel','Fabriquant')
        extra_kwargs = {'password' : {'write_only' : True}}

class AdministratuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administratuer
        fields = ('password', 'email')
        extra_kwargs = {'password': {'write_only': True}}



