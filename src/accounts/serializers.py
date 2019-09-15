from rest_framework import serializers

from accounts.models import Automobiliste, Fabriquant
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


class UtilisateurFabriquantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabriquant
        fields = ('email','password','nom','prenom','adresse','tel','marque')
        extra_kwargs = {'password' : {'write_only' : True}}
        read_only_fields = ('marque',)

    def create(self, validated_data):
        return Fabriquant.objects.create_user(**validated_data)

class AdminFabriquantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fabriquant
        fields = ('email','password','nom','prenom','adresse','tel','marque')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        return Fabriquant.objects.create_superuser(**validated_data)

class UtilisatuerFabriquantSerializerByAdmin(AdminFabriquantSerializer):

    def create(self, validated_data):
        return Fabriquant.objects.create_user(**validated_data)


class UpdateFabriquantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabriquant
        fields = ('email', 'password', 'nom', 'prenom', 'adresse', 'tel')
        extra_kwargs = {'password': {'write_only': True}}

        #TODO ensure that the admin can update the password

class ActiveFabriquantSerilizer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabriquant
        fields = ('email', 'password', 'nom', 'prenom', 'adresse', 'tel', 'is_active')
        read_only_fields = ('marque',)
        extra_kwargs = {'password': {'write_only': True}}


class AdministratuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrateur
        fields = ('password', 'email')
        extra_kwargs = {'password': {'write_only': True}}



