

from django.db import models
from couleur.models import Couleur
from accounts.models import Automobiliste
from option.models import Option
from modele.models import Modele
from version.models import Version
from marque.models import Marque


class Vehicule_Compose(models.Model):
    Automobiliste = models.ForeignKey(Automobiliste, on_delete=models.CASCADE)
    Modele = models.ForeignKey(Modele,on_delete=models.CASCADE)
    Version = models.ForeignKey(Version,on_delete=models.CASCADE)
    Couleur = models.ForeignKey(Couleur,on_delete=models.CASCADE)
    Options = models.ManyToManyField(Option)
    Prix_Total= models.FloatField(default=0.0)

    def get_marque(self):
      try:
          modele = Modele.objects.get(Code_Modele=self.Modele.Code_Modele)
          marque = modele.Id_Marque
          return marque.Id_Marque
      except:
          return "introuvable"

class Compose_Option(models.Model):
    option = models.ForeignKey(Option,on_delete=models.CASCADE)
    vehicule_compose = models.ForeignKey(Vehicule_Compose,on_delete=models.CASCADE)


