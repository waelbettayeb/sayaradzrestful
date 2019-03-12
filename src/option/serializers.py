from rest_framework import serializers

from option.models import Option


class Option_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = [
            'Code_Option',
            'Nom_Option',
        ]
