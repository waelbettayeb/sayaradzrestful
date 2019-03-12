from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from accounts.models import Fabriquant, User, UtilisateurFabriquant
from marque.models import Marque


class FabriquantTestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        fabriquant_1 = Fabriquant.objects.create_user("fk_zaidi@esi.dz",
                                                            password="testpassword",
                                                            nom ="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel= "023228511",
                                                            marque= renault
                                                            )
        fabriquant_1.save()

        user_fabriquant_1 = UtilisateurFabriquant.objects.create_user("fk_zaidi_user@esi.dz",
                                                            password="testpassword",
                                                            nom="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel="023228511",
                                                            fabriquant= fabriquant_1
                                                            )
        user_fabriquant_1.save()



    def test_list_fabriquant(self):
        client = APIClient()
        response = client.get('/accounts/fabriquant')
        assert response.status_code == 200
        assert len(response.data) == 1

    def test_create_fabriquant(self):

        client = APIClient()
        data = {
            'email' : 'hamza.kmsi@hotmail.com',
            'password' : 'test123',
            'nom' : 'ZAIDI',
            'prenom' : 'Hamza',
            'adresse' : "Cheraga",
            'tel' : '023228511',
            'marque': 1
        }

        response = client.post('/accounts/fabriquant', data=data)
        assert response.status_code == 400

        peugeot = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeot.save()
        data = {
            'email': 'hamza.kmsi@hotmail.com',
            'password': 'test123',
            'nom': 'ZAIDI',
            'prenom': 'Hamza',
            'adresse': "Cheraga",
            'tel': '023228511',
            'marque': 2
        }

        old_number = len(client.get('/accounts/fabriquant').data)
        response = client.post('/accounts/fabriquant', data =  data)
        assert response.status_code == 201
        response = client.get('/accounts/fabriquant')
        assert len(response.data) == (old_number+1)


class UtilisateurFabriquantTestCases(APITestCase):


    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        fabriquant_1 = Fabriquant.objects.create_user("fk_zaidi@esi.dz",
                                                            password="testpassword",
                                                            nom ="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel= "023228511",
                                                            marque= renault
                                                            )
        fabriquant_1.save()
        print(fabriquant_1)

        utilisateur_fabriquant = UtilisateurFabriquant.objects.create_user(
            email= 'test@renault.com',
            password='testpass',
            nom='test',
            prenom='test',
            adresse='test',
            tel='test',
            fabriquant = fabriquant_1

        )
        utilisateur_fabriquant.save()

    def test_create_utilisateur_fabriquant(self):
        client = APIClient()
        response = client.get('/accounts/fabriquant/utilisateur')
        assert response.status_code == 200
        old_len = len(response.data)

        data = {
            'email' : "test@renault.fr",
            'password' : 'pass1235',
            'nom':'test',
            'prenom' : 'test',
            'addresse' : 'adresse',
            'tel' : '0218512355',
            'Fabriquant' : "fk_zaidi@esi.dz"
        }

        response = client.post('/accounts/fabriquant/utilisateur',data)
        assert response.status_code == 201
        response = client.get('/accounts/fabriquant/utilisateur')
        assert len(response.data) == (old_len+1)
