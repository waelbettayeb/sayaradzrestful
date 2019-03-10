from rest_framework import serializers
from marque.models import Marque


class MarqueSereializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = [
            'Nom_Marque',
            'Id_Marque'
           # 'Logo_Marque'
        ]
