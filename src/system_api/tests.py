from django.test import TestCase
import pytest
import unittest
from django.test import Client
from .views import *
from rest_framework import status
from django.urls import reverse


class Test_list(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.marque2 = Marque.objects.create('m2', 'Marque2')
        self.modele1 = Modele.objects.create('mod1', 'modele1', 'm1')
        self.modele2 = Modele.objects.create('mod2', 'modele2', 'm2')
        self.version1 = Version.objects.create('v1', 'version1', 'mod1')
        self.version2 = Version.objects.create('v2', 'version2', 'mod2')
        self.version3 = Version.objects.create('v3', 'version3', 'mod2')

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

    """ def Test_Marque_Content(self):
        marques = Marque.objects.get()
        url = reverse('list_Marque')
        response = self.client.get(url)
        exp_data = {
            {'Id_Marque': 'm1',
            'Nom_Marque':'Marque1'
            },
            {'Id_Marque': 'm2',
            'Nom_Marque':'Marque2'}
        }
        self.asssertEqual(exp_data, response.json())
"""