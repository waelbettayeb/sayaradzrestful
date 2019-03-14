from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from . import models

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class AutomobilisteInline(admin.StackedInline):
    model = models.Automobiliste
    can_delete = False
    verbose_name_plural = 'automobiste'
class UserAdmin(BaseUserAdmin):
    list_display = ('email','password')
    inlines = (AutomobilisteInline)


admin.site.register(models.User)
admin.site.register(models.Automobiliste)
admin.site.register(models.Fabriquant)
admin.site.register(models.Administrateur)
