from rest_framework import serializers

from src.system_api.models import *


class Marque_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque',
            'Logo_Marque'
        ]

class Modele_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Modele
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque',
            'Photo_modele'
        ]
class Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = [
            'Code_Version',
            'Nom_Version',
            'Nom_Model'
        ]