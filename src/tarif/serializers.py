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


class FileUploadSerializer(serializers.Serializer):
    # I set use_url to False so I don't need to pass file
    # through the url itself - defaults to True if you need it
    file = serializers.FileField(use_url=False)