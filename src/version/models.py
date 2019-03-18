from django.db import models

# Create your models here.
from modele.models import Modele
from option.models import Option


class Version(models.Model):
    Code_Version = models.CharField(max_length=20, primary_key=True)
    Nom_Version = models.CharField(max_length=200)
    Id_Modele = models.ForeignKey(Modele, on_delete=models.CASCADE, related_name='Version_set')
    option_Version = models.ManyToManyField(Option, through='Option_Version',through_fields=('version', 'option', 'Default'))

class Option_Version(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    version = models.ForeignKey(Version, on_delete=models.CASCADE)
    Default = models.BooleanField(default=False)

    def get_default(self):
        return self.Default