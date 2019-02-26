from rest_framework import serializers

from src.system_api.models import Modele


class ModelSereializer(serializers.ModelSerializer):

    class Meta:
        model = Modele
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque'
        ]