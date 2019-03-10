from rest_framework import serializers

from modele.models import Modele


class Modele_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Modele
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque'
        ]
