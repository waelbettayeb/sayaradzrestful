from django.db import models
import datetime

from modele.models import Modele
from version.models import Version
from couleur.models import Couleur
from option.models import Option
# Create your models here.


class Tarif(models.Model):
    Prix = models.FloatField(blank=None, default=0.0)
    Date_Debut = models.DateField(blank=None, default=datetime.date.today)
    Date_Fin = models.DateField(blank=None, default=datetime.date.today)

class Tarif_Version(Tarif):
    Version = models.ForeignKey(Version,on_delete=models.CASCADE)

class Tarif_Option(Tarif):
    Option = models.ForeignKey(Option,on_delete=models.CASCADE)

class Tarif_Couleur(Tarif):
    Couleur = models.ForeignKey(Couleur,on_delete=models.CASCADE)