from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Annonce)
admin.site.register(Annonce_Image)
admin.site.register(Annonce_Option)