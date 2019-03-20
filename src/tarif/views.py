from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from tarif.models import Tarif_Version, Tarif_Option, Tarif_Couleur
from tarif.serializers import Tarif_Version_Sereializer, Tarif_Option_Sereializer, Tarif_Couleur_Sereializer
from tarif.tarif_management.Tarif_Builder import Tarif_Builder
# Create your views here.

class Tarif_Version_List(ListAPIView):
    serializer_class = Tarif_Version_Sereializer

    def get_queryset(self):
        version = self.kwargs['Code_Version']
        return Tarif_Version.objects.filter(Version = version)

#     =====================================================================================

class Tarif_Option_List(ListAPIView):
    serializer_class = Tarif_Option_Sereializer

    def get_queryset(self):
        option = self.kwargs['Code_Option']
        return Tarif_Version.objects.filter(Option = option)

#     =====================================================================================

class Tarif_Couleur_List(ListAPIView):
    serializer_class = Tarif_Couleur_Sereializer

    def get_queryset(self):
        couleur = self.kwargs['Code_Couleur']
        return Tarif_Version.objects.filter(Couleur = couleur)

#     =====================================================================================


class test(APIView):

    def post(self, request):
        # form = DocumentForm(request.POST, request.FILES)
        # if form.is_valid():
            # newdoc = Document(docfile = request.FILES['docfile'])
        newdoc = request.FILES['filename']
        tarif_builder = Tarif_Builder()
        if (tarif_builder.Tarif_Handle(newdoc)):
            return Response(status=201)

        return Response(status=204)
    def get (self,request):
        return render(request, 'list.html', {'documents': '', 'form': ''})
        # form = DocumentForm()  # A empty, unbound form

        # Load documents for the list page
        # documents = Document.objects.all()

        # Render list page with the documents and the form
