from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, \
    UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import marque
from accounts.models import Fabriquant, User
from accounts.serializers import ChangePasswordSerializer
from . import serializers
from . import models
from . import permissions
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

class FabriquantView(CreateAPIView):

    """Offre un end point pour créer des utilisatuers fabriquant
        L'utilisatuer doit être authentifé en tant qu'administrateur ou administrateur fabriquant
    """
    permission_classes = [IsAuthenticated, permissions.CanCreateUsers]
    authentication_classes = [OAuth2Authentication, ]
    serializer_class = serializers.UtilisateurFabriquantSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        if self.request.user.is_admin_fabriquant:
            admin_fabriquant = Fabriquant.objects.get(email= self.request.user)
            serializer.save(marque = admin_fabriquant.marque)
        else:
            serializer.save()

    def get_serializer_class(self):
        user = self.request.user
        if user.is_admin:
            return serializers.UtilisatuerFabriquantSerializerByAdmin
        else:
            return self.serializer_class

class ListUtilisateurFabriquantView(ListAPIView):

    """ Offre un end point pour lister les utilisateurs d'un fabriquant.
        L'utilisatuer doit être authentifé en tant qu'administrateur ou administrateur fabriquant
        Les administrateur fabriquant peuvent voir leurs prores utilisateurs
        L'administrateur peut voir les utilisateurs de tout les fabriquants
    """
    serializer_class = serializers.ActiveFabriquantSerilizer
    permission_classes = [permissions.IsUsersOwner, IsAuthenticated]
    authentication_classes = [OAuth2Authentication, ]
    lookup_field = 'marque'
    def get_queryset(self):
        id_marque = self.kwargs['Id_Marque']
        self.check_object_permissions(self.request, id_marque)
        return Fabriquant.objects.filter(marque = id_marque)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AdminFabriquantCreation(CreateAPIView):

    """ Offre un end point pour la création des administrateur fabriquant
        Les administrateur de fabriquant peuvent créer leurs propre compte
        ou leurs compte pevent être créés par l'administrateur
        Assure que un seul administrateur est crée par fabriquant
    """
    serializer_class = serializers.AdminFabriquantSerializer
    permission_classes = [permissions.CanCreateAdminFabriquant,  ]
    authentication_classes = [OAuth2Authentication, ]

    def post(self, request, *args, **kwargs):
        self.check_object_permissions(request,request)
        return super().post(request, *args, **kwargs)


class RUDUtilisateurFabriquant(RetrieveUpdateDestroyAPIView):

    """ Offre un end point pour :
        Voir les détail d'un utilisateur
        Modifier les données d'un utilisateur
        Supprimer un utilisateur
    """
    serializer_class = serializers.UtilisateurFabriquantSerializer
    permission_classes = (IsAuthenticated, permissions.CanUpdateUtilisateurFabriquant)
    authentication_classes = [OAuth2Authentication, ]
    lookup_field = 'email'

    def get_queryset(self):
        return Fabriquant.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PATCH' or 'GET':
            return serializers.ActiveFabriquantSerilizer
        return self.serializer_class

class UserType(APIView) :

    permission_classes = (IsAuthenticated, permissions.CanSeeType,  )
    authentication_classes = (OAuth2Authentication, )
    def get(self, request):
        user = request.user
        response = {}
        status = 200
        if user.is_admin :
            response['type'] = 'Administrateur'
        elif user.is_admin_fabriquant:
            response['type'] = 'Administrateur Fabriquant'
            fabriquant = Fabriquant.objects.get(email=user.email)
            user_serializer = serializers.AdminFabriquantSerializer(fabriquant)
            response['user'] = user_serializer.data
            fabriquant_marque = marque.models.Marque.objects.get(Id_Marque = fabriquant.marque.Id_Marque)
            marque_serializer = marque.serializers.Marque_Sereializer(fabriquant_marque)
            response['marque'] = marque_serializer.data
        elif user.is_fabriquant :
            response['type'] = 'Utilisateur Fabriquant'
            fabriquant = Fabriquant.objects.get(email=user.email)
            serializer = serializers.UtilisateurFabriquantSerializer(fabriquant)
            response['user'] = serializer.data
            fabriquant_marque = marque.models.Marque.objects.get(Id_Marque=fabriquant.marque.Id_Marque)
            marque_serializer = marque.serializers.Marque_Sereializer(fabriquant_marque)
            response['marque'] = marque_serializer.data
        else:
            response['error'] = 'Bad Request'
            status = 400

        return Response(data= response, status = status)

class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated, permissions.IsUsersOwner)

        def get_object(self, queryset=None):
            obj = User.objects.get(email = self.request.data['email'])
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response("Success.", status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

