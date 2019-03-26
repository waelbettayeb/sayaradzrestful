from django.db import models

# Create your models here.
import datetime

from rest_framework.utils import json

from accounts.models import Automobiliste
from couleur.models import Couleur
from modele.models import Modele
from option.models import Option
from version.models import Version

import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys = True, indent = 4)


class Vehicule(models.Model):
    Numero_Chassis = models.CharField(max_length = 20, primary_key = True)
    Concessionnaire = models.CharField(max_length = 50, default ="")
    Code_Version = models.ForeignKey(Version, on_delete = models.CASCADE)
    Code_Couleur = models.ForeignKey(Couleur, on_delete = models.CASCADE)
    Liste_Option = models.ManyToManyField(Option, through = 'List_option',through_fields=('vehicule', 'option'))
    Reservation = models.ManyToManyField(Automobiliste, through = 'Commande',through_fields=('vehicule', 'automobiliste'))

    def get_marque(self):
        try :
            version = Version.objects.get(Code_Version =  self.Code_Version.Code_Version)
            modele = Modele.objects.get(Code_Modele = version.Id_Modele.Code_Modele)
            marque = modele.Id_Marque
            return marque.Id_Marque
        except :
            return "introuvable"

    def get_modele(self):
        try :
            version = Version.objects.get(Code_Version =  self.Code_Version.Code_Version)
            modele = version.Id_Modele
            return modele.Code_Modele
        except :
            return "introuvable"


class List_Option(models.Model):
    option = models.ForeignKey(Option, on_delete = models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete = models.CASCADE)

    def get_option(self):
        return Option.objects.get(Code_Option = self.option.Code_Option).Nom_Option


class Commande(models.Model):
    automobiliste = models.ForeignKey(Automobiliste, on_delete = models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, on_delete = models.CASCADE)
    date = models.DateField(blank = None, default = datetime.date.today)
    montant = models.FloatField(blank = None, default=0.0)
    reserver = models.BooleanField(default = False)

    def get_marque(self):
        try :
            vehicule = Vehicule.objects.get(Numero_Chassis =  self.vehicule.Numero_Chassis)
            version = Version.objects.get(Code_Version =  vehicule.Code_Version.Code_Version)
            modele = Modele.objects.get(Code_Modele = version.Id_Modele.Code_Modele)
            marque = modele.Id_Marque
            return marque.Id_Marque
        except :
            return "introuvable"