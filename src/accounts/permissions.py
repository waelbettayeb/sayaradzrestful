from rest_framework import permissions

from accounts import serializers
from accounts.models import Automobiliste, User


class IsAutomobiliste(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_automobiliste

class IsAdminFabriquant(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_admin_fabriquant

class IsUserFabriquant(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_fabriquant

class IsAdminstrateur(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin


class IsUsersOwner(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.user.is_anonymous :
            return False

        return request.user.is_admin or request.user.is_admin_fabriquant

    def has_object_permission(self, request, view, obj):

        if request.user.is_anonymous :
            return False

        if request.user.is_admin :
            return True

        if request.user.is_admin_fabriquant :
            perimssion = int(request.user.marque.Id_Marque) == obj
            print(perimssion)
            return perimssion

