from rest_framework import serializers

from couleur.models import Couleur


class Couleur_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Couleur
        fields = [
            'Code_Couleur',
            'Nom_Couleur'
        ]
