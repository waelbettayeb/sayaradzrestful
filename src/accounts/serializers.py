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


class FabriquantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabriquant
        fields = ('email','password','nom','prenom','adresse','tel','marque')
        extra_kwargs = {'password' : {'write_only' : True}}

class UpdateFabriquantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fabriquant
        fields = ('email', 'password', 'nom', 'prenom', 'adresse', 'tel')
        extra_kwargs = {'password': {'write_only': True}}

        #TODO ensure that the admin can update the password



class AdminFabriquantSerializer(FabriquantSerializer):

    def create(self, validated_data):
        return Fabriquant.objects.create_superuser(**validated_data)


# class UtilisateurFabrquantSerailizer(serializers.ModelSerializer):
#     class Meta:
#         model = models.UtilisateurFabriquant
#         fields = ('email','password','nom','prenom','tel','Fabriquant')
#         extra_kwargs = {'password' : {'write_only' : True}}

class AdministratuerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Administrateur
        fields = ('password', 'email')
        extra_kwargs = {'password': {'write_only': True}}



