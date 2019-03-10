from rest_framework import permissions

from accounts import serializers
from accounts.models import Automobiliste, User


class IsAutomobiliste(permissions.BasePermission):

    def has_permission(self, request, view):
        is_automobiliste = False
        queryset = Automobiliste.objects.all()
        if request.user in queryset :
            is_automobiliste = True

        return is_automobiliste
