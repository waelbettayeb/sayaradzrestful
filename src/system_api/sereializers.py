from rest_framework import serializers
from system_api.models import *

class Marque_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = [
            'Nom_Marque',
            'Id_Marque'
           # 'Logo_Marque'
        ]


class Modele_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Modele
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque'
        ]
class Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = [
            'Nom_Version',
            'Code_Version',
            'Id_Modele'
        ]