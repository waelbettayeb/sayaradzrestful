from rest_framework import serializers

from tarif.models import Tarif_Version,Tarif_Couleur,Tarif_Option


class Tarif_Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Tarif_Version
        fields = [
            'Prix',
            'Date_Debut',
            'Date_Fin'
        ]


class Tarif_Option_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Tarif_Option
        fields = [
            'Prix',
            'Date_Debut',
            'Date_Fin'
        ]


class Tarif_Couleur_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Tarif_Couleur
        fields = [
            'Prix',
            'Date_Debut',
            'Date_Fin'
        ]

