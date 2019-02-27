from rest_framework import serializers

from system_api.models import Marque

from system_api.models import Modele

from system_api.models import Version



class Marque_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = [
            'Nom_Marque',
            'Id_Marque'
        ]



class Modele_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Modele
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque'
        ]
class VersionSereializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = [
            'Code_Version',
            'Nom_Version',
            'Nom_Model'
        ]