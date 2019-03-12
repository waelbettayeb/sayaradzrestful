from rest_framework import permissions

from accounts import serializers
from accounts.models import Automobiliste, User


class IsAutomobiliste(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_automobiliste
