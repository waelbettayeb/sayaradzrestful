from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from accounts.models import Fabriquant, User


class FabriquantTestCases(APITestCase):

    def setUp(self):

        fabriquant_1 = Fabriquant.objects.create_fabriquant("fk_zaidi@esi.dz",
                                                            password="testpassword",
                                                            nom ="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel= "023228511")
        fabriquant_1.save()

        user = User.objects.create_user("hamza.kmsi@gmail.com")
        user.save()



    def test_list_fabriquant(self):
        client = APIClient()
        response = client.get('/accounts/fabriquant')
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_create_fabriquant(self):

        client = APIClient()
        request_factory = APIRequestFactory()
        data = {
            'email' : 'hamza.kmsi@hotmail.com',
            'password' : 'test123',
            'nom' : 'ZAIDI',
            'prenom' : 'Hamza',
            'adresse' : "Cheraga",
            'tel' : '023228511'
        }
        old_number = len(client.get('/accounts/fabriquant').data)
        response = client.post('/accounts/fabriquant', data =  data)
        assert response.status_code == 201
        response = client.get('/accounts/fabriquant')
        assert len(response.data) == (old_number+1)