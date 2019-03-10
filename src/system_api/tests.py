import json
from django.test import TestCase
import pytest
import unittest
from django.test import Client
from .views import *
from rest_framework import status
from django.urls import reverse


class Test_list(unittest.TestCase):

"""
    def Test_Marque(self):
        url = reverse('list_Marque')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def Test_Model(self):
        url = reverse('list_Model')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def Test_Version(self):
        url = reverse('list_Version')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""
from rest_framework.test import APITestCase, APIClient

from system_api.models import *


class ModelesAPITestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')

        symbol  = Modele.objects.create(Code_Modele = 'm1', Nom_Modele = 'Symbol', Id_Marque = renault)
        fluance = Modele.objects.create(Code_Modele = 'm2', Nom_Modele = 'fluence', Id_Marque = renault)
        symbol.save()
        fluance.save()

        _206 = Modele.objects.create(Code_Modele='m3', Nom_Modele='206', Id_Marque=peugeaut)
        _207 = Modele.objects.create(Code_Modele='m4', Nom_Modele='207', Id_Marque=peugeaut)
        _206.save()
        _207.save()

    def test_retrieve_all_models(self):

        """
        Vérifie la réussite de GET Request pour récupérer la liste des modèles.
        :return:
        """
        client = APIClient()
        response = client.get('/Automobiliste/consultations/listmodel',format = 'json')
        assert response.status_code == 200



class MarquesAPITestCases(APITestCase):
    def setUp(self):
        marque = Marque.objects.create(Id_Marque=1, Nom_Marque='BMW')
        marque.save()
        modele = Modele.objects.create(Code_Modele=1, Nom_Modele='MODELE',Id_Marque=1)
        marque.save()
        version=Version.objects.create(Code_Version=1,Nom_Version='Version',Id_Modele=1)
    def test_retrieve_all_marques(self):
        """Test si le client est capable de retrouver toutes les marques avec un get request"""
        client = APIClient()
        response = client.get('/Automobiliste/consultations/listmarque', format = 'json')
        assert response.status_code == 200
        response_data = json.loads((response.content.decode('utf-8')))
        self.assertEqual(response_data, '[{"model": "system_api.marque", "pk": "1", "fields": {"Nom_Marque": "BMW"}}]')
    def test_retrieve_all_versions(self):
        """Test si le client est capable de retrouver toutes les marques avec un get request"""
        client = APIClient()
        response = client.get('/Automobiliste/consultations/listVersion', format = 'json')
        assert response.status_code == 200
        response_data = json.loads((response.content.decode('utf-8')))
        self.assertEqual(response_data, '[{"model": "system_api.marque", "pk": "1", "fields": {"Nom_Version": "Version"},{"Id_Modele": "1"}}]')

<<<<<<< HEAD
=======
# Create your tests here.
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json

from system_api.models import Marque, Modele


class ModelesAPITestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')

        symbol  = Modele.objects.create(Code_Modele = 'm1', Nom_Modele = 'Symbol', Id_Marque = renault)
        fluance = Modele.objects.create(Code_Modele = 'm2', Nom_Modele = 'fluence', Id_Marque = renault)
        symbol.save()
        fluance.save()

        _206 = Modele.objects.create(Code_Modele='m3', Nom_Modele='206', Id_Marque=peugeaut)
        _207 = Modele.objects.create(Code_Modele='m4', Nom_Modele='207', Id_Marque=peugeaut)
        _206.save()
        _207.save()

    def test_retrieve_all_models(self):

        """
        Vérifie la réussite de GET Request pour récupérer la liste des modèles.
        :return:
        """
        client = APIClient()
        response = client.get('/Automobiliste/consultations/listmodel',format = 'json')
        assert response.status_code == 200


        # response_data = json.loads((response.content.decode('utf-8')))
        # print(len(response_data))







class MarquesAPITestCases(APITestCase):
    def setUp(self):
        marque = Marque.objects.create(Id_Marque=1, Nom_Marque='BMW')
        marque.save()

    def test_retrieve_all_marques(self):

        """Test si le client est capable de retrouver toutes les marques avec un get reques"""

        client = APIClient()
        response = client.get('/Automobiliste/consultations/listmarque', format = 'json')
        assert response.status_code == 200
        response_data = json.loads((response.content.decode('utf-8')))
        self.assertEqual(response_data, '[{"model": "system_api.marque", "pk": "1", "fields": {"Nom_Marque": "BMW"}}]')


>>>>>>> bf524187a852c6aaf734beb26a3840a13a04c722
