from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.serializers import serialize
import json

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
        'Nom_Marque'
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
