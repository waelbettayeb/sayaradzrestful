from rest_framework import serializers

from src.system_api.models import Modele
from src.system_api.models import Version



class ModelSereializer(serializers.ModelSerializer):

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