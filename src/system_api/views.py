from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
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

def testlist(request):

    obj = Modele.objects.all()
    data = serialize("json",obj,fields=(
        'Id_Marque',
        'Code_Modele',
        'Nom_Modele'
    ))
    print(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(json_data)

# Create your views here.
