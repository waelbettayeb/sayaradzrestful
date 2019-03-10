from django.db import models

# Create your models here.
from modele.models import Modele


class Version(models.Model):
    Code_Version = models.CharField(max_length=20, primary_key=True)
    Nom_Version = models.CharField(max_length=200)
    Id_Modele = models.ForeignKey(Modele, on_delete=models.CASCADE, related_name='Version_set')


