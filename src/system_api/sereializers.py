from rest_framework import serializers

from system_api.models import Marque

from system_api.models import Modele


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