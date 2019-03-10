from rest_framework import serializers
<<<<<<< HEAD
from src.system_api.models import *
=======

from system_api.models import Marque, Version

from system_api.models import Modele
>>>>>>> bf524187a852c6aaf734beb26a3840a13a04c722


class Marque_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Marque
        fields = [
            'Nom_Marque',
            'Id_Marque'
           # 'Logo_Marque'
        ]


class Modele_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Modele
        fields = [
            'Code_Modele',
            'Nom_Modele',
            'Id_Marque'
        ]
class Version_Sereializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = [
            'Nom_Version',
            'Code_Version',
            'Id_Modele'
        ]