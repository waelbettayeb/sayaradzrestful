from django.contrib import admin

# Register your models here.
from version.models import Version, Option_Version

admin.site.register(Version)
admin.site.register(Option_Version)