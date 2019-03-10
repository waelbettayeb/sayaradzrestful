from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json

from marque.models import Marque
from marque.serializers import MarqueSereializer
from modele.models import Modele
from version.models import Version


class MarquesAPITestCases(APITestCase):
    def setUp(self):
        marque = Marque.objects.create(Id_Marque=1, Nom_Marque='BMW')
        marque.save()
        modele = Modele.objects.create(Code_Modele=1, Nom_Modele='MODELE',Id_Marque=marque)
        marque.save()
        version=Version.objects.create(Code_Version=1,Nom_Version='Version',Id_Modele=modele)

    def test_retrieve_all_marques(self):
        """Test si le client est capable de retrouver toutes les marques avec un get request"""
        client = APIClient()
        response = client.get('/marque', format = 'json')
        marques = Marque.objects.all()
        serializer = MarqueSereializer(marques, many=True)
        assert response.status_code == 200
        #assert len(response.data) == 1
        #self.assertEqual(serializer.data, response.data)
        print(response.data)