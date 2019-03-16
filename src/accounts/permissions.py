from rest_framework import permissions

from accounts import serializers
from accounts.models import Automobiliste, User, Fabriquant


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
            return perimssion

class CanCreateAdminFabriquant(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_anonymous or request.user.is_admin

    def has_object_permission(self, request, view, obj):
        return Fabriquant.objects.has_admin(request.data['marque']) == False


class CanUpdateUtilisateurFabriquant(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        return user.is_admin or user.is_admin_fabriquant or  user.is_fabriquant

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_admin:
            return True

        if user.is_admin_fabriquant:
            permission = str(user.marque) == str(obj.marque)
            if 'is_active' in request.data.keys():
                permission = permission and str(user.email) != str(obj.email)
            return permission

        if user.is_fabriquant:
            if 'is_active' in request.data.keys():
                return False
            if request.method == 'DELETE':
                return False
            return str(user.email) == (obj.email)
