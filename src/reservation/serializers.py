
from rest_framework import serializers

from reservation.disponibilité.Option_Vehicule import Options_de_vehicule
from reservation.models import Vehicule, List_Option, Commande


class Vehicule_Sereializer(serializers.ModelSerializer):
    Marque = serializers.SerializerMethodField()
    Modele = serializers.SerializerMethodField()

    class Meta:
        model = Vehicule
        fields = [
            'Numero_Chassis',
            'Marque',
            'Modele',
            'Code_Version',
            'Code_Couleur',
            'Liste_Option',
            'Reservasion'

        ]

    def get_Marque(self,object):
        return object.get_marque()

    def get_Modele(self,object):
        return object.get_modele()

class Vehicule_Sereializer_Disp(serializers.ModelSerializer):
    Marque = serializers.SerializerMethodField()
    Modele = serializers.SerializerMethodField()
    options_vehicule = serializers.SerializerMethodField()

    class Meta:
        model = Vehicule
        fields = [
            'Numero_Chassis',
            'Marque',
            'Modele',
            'Code_Version',
            'Code_Couleur',
            'options_vehicule',
            'Reservasion'

        ]

    def get_Marque(self,object):
        return object.get_marque()

    def get_Modele(self,object):
        return object.get_modele()

    def get_options_vehicule(self,object):
        t = Options_de_vehicule()
        return t.get_options(object.Numero_Chassis)


class List_Option_Sereializer(serializers.ModelSerializer):
    nom_option = serializers.SerializerMethodField()
    class Meta:
        model = List_Option
        fields = [
            'option',
            'nom_option'
        ]
    def get_nom_option(self,object):
        return object.get_option()

class Commande_Sereializer(serializers.ModelSerializer):
    Marque = serializers.SerializerMethodField()

    class Meta:
        model = Commande
        fields = [
            'automobiliste',
            'vehicule',
            'date',
            'montant',
            'reserver',
            'Marque'
        ]
    def get_Marque(self,object):
        return object.get_marque()


class Options_Vehicule_Sereializer(serializers.ModelSerializer):
    options_vehicule = serializers.SerializerMethodField()

    class Meta:
        model = Vehicule
        fields = [
            'Numero_Chassis',
            'options_vehicule'
        ]

    def get_options_vehicule(self,object):
        t = Options_de_vehicule()
        return t.get_options(object.Numero_Chassis)
