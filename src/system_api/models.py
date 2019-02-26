# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

class Marque(models.Model):
    Id_Marque = models.CharField(max_length=10, primary_key=True)
    Nom_Marque = models.CharField(max_length=100)

class Modele(models.Model):
    Code_Modele = models.CharField(max_length=10, primary_key=True)
    Nom_Modele = models.CharField(max_length=100)
    Id_Marque = models.ForeignKey(Marque, on_delete=models.CASCADE)

class Version(models.Model):
    Code_Version = models.CharField(max_length=20, primary_key=True)
    Nom_Version = models.CharField(max_length=200)
    Nom_Model = models.ForeignKey(Modele, on_delete=models.CASCADE)


class Option(models.Model):
    Code_Option = models.CharField(max_length=20, primary_key=True)
    Nom_Option = models.CharField(max_length=100)

class Compatible(models.Model):
    Code_Version = models.ForeignKey(Version, on_delete=models.CASCADE)
    Code_Option = models.ForeignKey(Option, on_delete=models.CASCADE)
    defaut = models.BooleanField()

    class Meta:
        unique_together = (("Code_Version","Code_Option"),)



# Create your models here.