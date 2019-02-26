from django.contrib import admin
from .models import Marque
from .models import Modele

# Register your models here.

admin.site.register(Marque)
admin.site.register(Modele)