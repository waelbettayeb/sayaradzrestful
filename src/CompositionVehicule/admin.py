from django.contrib import admin

# Register your models here.
from CompositionVehicule.models import Vehicule_Compose,Compose_Option

admin.site.register(Vehicule_Compose)
admin.site.register(Compose_Option)