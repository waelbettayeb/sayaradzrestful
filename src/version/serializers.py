from rest_framework import serializers

from version.models import Version, Option_Version


class Version_Sereializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = [
            'Nom_Version',
            'Code_Version'
        ]
class Option_Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Option_Version
        fields = [
            'option',
            'version',
            'Default'
        ]



class Version_Option_Sereializer(serializers.ModelSerializer):


    class Meta:
        model = Version
        fields = [
            'Nom_Version',
            'Code_Version',
            'option_Version'
        ]