from django.db import models

# Create your models here.


class Option(models.Model):
    Code_Option = models.CharField(max_length=20, primary_key=True)
    Nom_Option = models.CharField(max_length=100)