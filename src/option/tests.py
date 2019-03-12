from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from marque.models import Marque
from modele.models import Modele
from version.models import Version
from option.models import Option


class OptionsAPITestCases(APITestCase):

    def setUp(self):

        peugeaut = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')

        symbol = Modele.objects.create(Code_Modele='m1', Nom_Modele='Symbol', Id_Marque=peugeaut)

        version = Version.objects.create(Code_Version='m3', Nom_Version='206', Id_Modele=symbol)
        version.save()

        option = Option.objects.create(Code_Option='m3', Nom_Option='206', Compatible=version)
        option.save()

    def test_retrieve_all_models(self):

        """
        Vérifie la réussite de GET Request pour récupérer la liste des options.
        :return:
        """
        client = APIClient()
        response = client.get('/option/',format = 'json')
        assert response.status_code == 200


