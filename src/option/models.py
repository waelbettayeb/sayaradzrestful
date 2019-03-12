from django.db import models

# Create your models here.
from version.models import Version


class Option(models.Model):
    Code_Option = models.CharField(max_length=10, primary_key=True)
    Nom_Option = models.CharField(max_length=100)
    Compatible = models.ManyToManyField(Version,through='Compatibilité',through_fields=('option','version'))
    # Defaut = models.ManyToManyField(Version,through='Defaut',through_fields=('option','version'))

class Compatibilité(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
#
# class Defaut(models.Model):
#     option = models.ForeignKey(Option, on_delete=models.CASCADE)
#     version = models.ForeignKey(Version, on_delete=models.CASCADE)
