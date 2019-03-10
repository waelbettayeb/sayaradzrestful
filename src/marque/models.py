from django.db import models

# Create your models here.


class Marque(models.Model):
    Id_Marque = models.CharField(max_length=10, primary_key=True)
    Nom_Marque = models.CharField(max_length=100)
    #Logo_Marque = models.ImageField(upload_to='Marque_logo', blank=True, null=True)

