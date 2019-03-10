from rest_framework import serializers

from version.models import Version


class Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = [
            'Nom_Version',
            'Code_Version',
            'Id_Modele'
        ]