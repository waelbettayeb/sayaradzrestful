import datetime

from django.db import models

from accounts.models import Automobiliste
from option.models import Option
from couleur.models import Couleur
from version.models import Version

from modele.models import Modele


class Annonce(models.Model):
    Prix_Minimal = models.FloatField(blank = None, default=0.0)
    Description = models.TextField(blank=True,null=True)
    Date_Annonce=models.DateField(blank = None, default = datetime.date.today)
    Id_Automobiliste = models.ForeignKey(Automobiliste,on_delete=models.CASCADE)
    Couleur = models.ForeignKey(Couleur, on_delete=models.CASCADE,null=True,blank=True)
    Version = models.ForeignKey(Version, on_delete=models.CASCADE,blank=True)
    Options_Annonce= models.ManyToManyField(Option,related_name='Annonces')

    def get_marque(self):

        try:
           version = Version.objects.get(Code_Version=self.Version.Code_Version)
           modele = Modele.objects.get(Code_Modele=version.Id_Modele.Code_Modele)
           marque = modele.Id_Marque
           return marque.Id_Marque
        except:
         return "introuvable"


    def get_modele(self):
      try:
          version = Version.objects.get(Code_Version=self.Version.Code_Version)
          modele = version.Id_Modele
          return modele.Code_Modele
      except:
          return "introuvable"


class Annonce_Option(models.Model):
    annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.annonce.Description+ " " + self.option.name
class Annonce_Image(models.Model):
    Images_Annonce = models.FileField(null=False, upload_to='Annonce/')
    Annonce = models.ForeignKey(Annonce, related_name='Images_Annonce',null=False,default=1,on_delete=models.CASCADE)