from django.contrib import admin

# Register your models here.
from option.models import Option, Compatibilite

admin.site.register(Option)
admin.site.register(Compatibilite)
