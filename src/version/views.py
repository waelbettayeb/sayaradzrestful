from rest_framework import generics
from rest_framework.generics import ListAPIView

# Create your views here.
from version.models import Version, Option_Version
from version.serializers import Version_Sereializer, Version_Option_Sereializer, Option_Version_Sereializer


class AllVerions(ListAPIView):
    serializer_class = Version_Sereializer

    def get_queryset(self):
        return Version.objects.all()

class VersionByModele(ListAPIView):
    serializer_class = Version_Sereializer

    def get_queryset(self):
        Id_Modele = self.kwargs.get('Id_Modele')
        return Version.objects.filter(Id_Modele = Id_Modele)

class NewVersion(generics.ListCreateAPIView):
    queryset = Version.objects.all()
    serializer_class = Version_Sereializer
    # permission_classes = (IsAdminUser,)


class option_version(ListAPIView):
    serializer_class = Option_Version_Sereializer

    def get_queryset(self):
        id_version = self.kwargs['Id_Version']
        return Option_Version.objects.filter(version=id_version).filter(Default = True)

