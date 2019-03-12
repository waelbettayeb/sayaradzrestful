from rest_framework import serializers
from marque.models import Marque


class Marque_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = [
            'Nom_Marque',
            'Id_Marque',
            'Logo'
        ]
