from django.contrib import admin

# Register your models here.
from reservation.models import Vehicule, Commande, List_Option

admin.site.register(Vehicule)
admin.site.register(Commande)
admin.site.register(List_Option)