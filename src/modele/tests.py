from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from marque.models import Marque
from modele.models import Modele


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
        response = client.get('/modele/',format = 'json')
        assert response.status_code == 200

    def test_retrieve_modele_by_marque(self):

        """ Verifie la requette sur un id de marque"""

        client = APIClient()
        response = client.get('/modele/1')
        assert response.status_code == 200

