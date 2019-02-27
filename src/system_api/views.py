from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.serializers import serialize
import json
from rest_framework.generics import ListAPIView

from system_api.sereializers import Marque_Sereializer

from system_api.sereializers import Modele_Sereializer
from .models import Marque, Modele



def testgetone(request):
    obj = Modele.objects.get(Id_Marque="b51")
    # obj = Modele.objects.all()
    data ={
        "name" : obj.Code_Modele,
        "doing" : obj.Nom_Modele
    }
    return JsonResponse(data)

def list_Marque(request):
    obj = Marque.objects.all()
    data = serialize("json", obj, fields=(
        'Id_Marque',
        'Nom_Marque',
        'Logo'
    ))
    print(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def list_Model(request):

    obj = Modele.objects.all()
    data = serialize("json",obj,fields=(
        'Id_Marque',
        'Code_Modele',
        'Nom_Modele'
    ))
    print(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')

def list_Model_Marque(request):
    # Q(Id_marque = request.GET. .get("Id"))
    obj = Modele.objects.filter(Q(Id_Marque = "c12"))
    data = serialize("json", obj, fields = (
        'Id_Marque',
        'Code_Modele',
        'Nom_Modele'
    ))
    print(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

# Create your views here.


class liste_Marque(ListAPIView):
    serializer_class = Marque_Sereializer

    def get_queryset(self):
        return Marque.objects.all()

class liste_Modele(ListAPIView):
    serializer_class = Modele_Sereializer

    def get_queryset(self):
        Id_Marque = self.kwargs.get('Id_Marque')
        mrq=get_object_or_404(Marque, Id_Marque=Id_Marque)

        return mrq.Model_set
