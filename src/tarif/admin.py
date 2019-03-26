from django.contrib import admin

# Register your models here.
from tarif.models import Tarif_Version,Tarif_Option,Tarif_Couleur

admin.site.register(Tarif_Version)
admin.site.register(Tarif_Option)
admin.site.register(Tarif_Couleur)