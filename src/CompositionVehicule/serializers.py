from django.db import transaction
from rest_framework import serializers
from couleur.models import Couleur
from tarif.models import Tarif,Tarif_Version,Tarif_Option,Tarif_Couleur
from accounts.serializers import  AutomobilisteSerializer
from option.serializers import Option_Sereializer
from CompositionVehicule.models import Vehicule_Compose,Compose_Option
from option.models import Option
from accounts.models import Automobiliste
from couleur.models import Couleur
from modele.models import Modele
from modele.serializers import Modele_Sereializer
from version.models import Version
from version.serializers import Version_Sereializer


class Couleur_Serializer(serializers.ModelSerializer):
    class Meta:
       model =Couleur
       fields = [
            'Code_Couleur',
            'Nom_Couleur',

        ]

class ComposeOptionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='option.Code_Option')
    name = serializers.ReadOnlyField(source='option.Nom_Option')

    class Meta:
        model = Compose_Option
        fields = ['id', 'name',]
class AutoRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "email")
        super(AutoRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class OptionRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Option")
        super(OptionRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class CouleurRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Couleur")
        super(CouleurRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)

class ModeleRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Modele")
        super(ModeleRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)
class VersionRelatedField(serializers.PrimaryKeyRelatedField):
    """A PrimaryKeyRelatedField derivative that uses named field for the display value."""

    def __init__(self, **kwargs):
        self.display_field = kwargs.pop("display_field", "Nom_Version")
        super(VersionRelatedField, self).__init__(**kwargs)

    def display_value(self, instance):
        # Use a specific field rather than model stringification
        return getattr(instance, self.display_field)


class Compose_Sereializer(serializers.HyperlinkedModelSerializer):
    automobiliste= AutomobilisteSerializer(read_only=True,many=False)
    Automobiliste = AutoRelatedField(queryset=Automobiliste.objects.all(), many=False)
    Couleur = CouleurRelatedField(queryset=Couleur.objects.all(), many=False)
    Modele = ModeleRelatedField(queryset=Modele.objects.all(), many=False)
    Options = OptionRelatedField(queryset=Option.objects.all(), many=True)
    Version = VersionRelatedField(queryset=Version.objects.all(), many=False)
    class Meta:
        model = Vehicule_Compose
        fields = ['automobiliste','Automobiliste','Couleur','Modele','Version','Options', 'Prix_Total']


    @transaction.atomic
    def create(self, validated_data):

        automobiliste = validated_data.pop('Automobiliste')
        Auto_instance = Automobiliste.objects.get(email=automobiliste.email)
        version = validated_data.pop('Version')
        version_instance = Version.objects.get(Code_Version=version.Code_Version)
        couleur = validated_data.pop('Couleur')
        couleur_instance= Couleur.objects.get(Code_Couleur=couleur.Code_Couleur)
        modele = validated_data.pop('Modele')
        modele_instance = Modele.objects.get(Code_Modele=modele.Code_Modele)
        prixCouleur = Tarif_Couleur.objects.get(Couleur=couleur.Code_Couleur).Prix
        prixVersion = Tarif_Version.objects.get(Version=version.Code_Version).Prix
        options = self.initial_data.get("Options")
        print(options)
        prix_Option=0.0
        int=0
        compose = Vehicule_Compose.objects.create(Automobiliste=Auto_instance,
                                                 Couleur=couleur_instance, Modele=modele_instance,Version =version_instance)
        for option in options:
              Option_instance = Option.objects.get(pk=option)
              option_Compose=Compose_Option.objects.create(vehicule_compose=compose, option=Option_instance)
              option_Compose.save()
              compose.Options.add(Option_instance)
              prix=Tarif_Option.objects.get(Option=Option_instance).Prix
              prix_Option=prix_Option+prix

        prix_total=prix_Option+prixCouleur+prixVersion
        compose.Prix_Total=prix_total
        compose.save()
        return compose


class VehiculeView_Sereializer(serializers.HyperlinkedModelSerializer):
    Options =Option_Sereializer(many=True, read_only=True)
    Couleur = Couleur_Serializer(many=False, read_only=True)
    Automobiliste = AutomobilisteSerializer(read_only=True, many=False)
    Modele = Modele_Sereializer(many=False, read_only=True)
    Version = Version_Sereializer(many=False, read_only=True)
    Marque = serializers.SerializerMethodField()
    class Meta:
        model = Vehicule_Compose
        fields = ('Automobiliste','Couleur','Marque', 'Modele','Version','Options','Prix_Total')

    def get_Marque(self, object):
        return object.get_marque()
