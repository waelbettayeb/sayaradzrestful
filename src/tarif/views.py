from rest_framework.generics import ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from tarif.models import Tarif_Version, Tarif_Option, Tarif_Couleur
from tarif.serializers import Tarif_Version_Sereializer,Tarif_Option_Sereializer,Tarif_Couleur_Sereializer

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

class File_Up_load(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.FILES['file']

        if (Tarif_Builder.Tarif_Handle(file_obj)):
            return Response(status=201)

        return Response(status=204)