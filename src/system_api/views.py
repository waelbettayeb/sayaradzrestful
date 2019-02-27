
from .models import Version
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from  rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
import json
from django.views import generic
from .models import *
from .sereializers import *

"""class list_Marque(generic.ListView):
    model = Marque
    serializers=Marque_Sereializer

    def get_queryset(self):
        return Marque.objects.all()


class list_modele(generic.ListView):
    model = Modele
    serializers = Modele_Sereializer
    def get_queryset(self):
        return Modele.objects.all()



"""

def list_Model(request):

    obj = Modele.objects.all()
    data = serialize("json", obj, fields=(
        'Id_Marque',
        'Code_Modele',
        'Nom_Modele'
    ))
    print(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(json_data)

def testgetone(request):
    obj = Modele.objects.get(Id_Marque="b51")
    data ={
        "name" : obj.Code_Modele,
        "doing" : obj.Nom_Modele
    }
    return JsonResponse(data)

def list_Version(request):
        Version_list = Version.objects.all()
        Serialized_Version = serialize("json", Version_list, fields=(
            'Nom_Model'
            'Code_Version'
            'Nom_Version'
        ))
        print(Serialized_Version)
        json_data = json.dumps(Serialized_Version)
        return HttpResponse(json_data, content_type='application/json')
        # return JsonResponse(json_data)

