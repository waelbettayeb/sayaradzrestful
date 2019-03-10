from django.db import models

# Create your models here.
from marque.models import Marque


class Modele(models.Model):
    Code_Modele = models.CharField(max_length=10, primary_key=True)
    Nom_Modele = models.CharField(max_length=100)
    Id_Marque = models.ForeignKey(Marque,on_delete=models.CASCADE, related_name='Model_set')

