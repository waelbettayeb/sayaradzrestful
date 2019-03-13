from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient, APIRequestFactory, force_authenticate

from accounts import serializers
from accounts.models import Fabriquant
from accounts.views import FabriquantView
from marque.models import Marque


class FabriquantTestCases(APITestCase):
    first_len = 0

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        peugeot = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeot.save()

        fabriquant_1 = Fabriquant.objects.create_user("fk_zaidi@esi.dz",
                                                            password="testpassword",
                                                            nom ="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel= "023228511",
                                                            marque= renault
                                                            )
        fabriquant_1.save()


        fabriquant_2 = Fabriquant.objects.create_user("fk_zaidi_test@esi.dz",
                                                            password="testpassword",
                                                            nom ="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel= "023228511",
                                                            marque= peugeot
                                                            )
        fabriquant_2.save()


    def test_list_fabriquant(self):

        factory = APIRequestFactory()
        user = Fabriquant.objects.get(email = "fk_zaidi@esi.dz")
        request = factory.get('/accounts/fabriquant/utilisateur')
        force_authenticate(request, user = user)
        view = FabriquantView.as_view()
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 1
        user_peugeot = Fabriquant.objects.get(email = "fk_zaidi_test@esi.dz")
        queryset = Fabriquant.objects.filter(marque=request.user.marque)
        assert not user_peugeot in queryset

    def test_create_fabriquant(self):
        factory = APIRequestFactory()
        user = Fabriquant.objects.get(email="fk_zaidi@esi.dz")
        data = {
            'email' : "test@test.com",
            'marque' : 2
        }
        request = factory.post('/accounts/fabriquant/utilisateur',data)
        force_authenticate(request, user=user)
        view = FabriquantView.as_view()
        response = view(request)
        print(response.data)
        assert response.status_code == 201
        # assert len(response.data) == 1
        # user_peugeot = Fabriquant.objects.get(email="fk_zaidi_test@esi.dz")
        # queryset = Fabriquant.objects.filter(marque=request.user.marque)
        # assert not user_peugeot in queryset

    def test_create_admin_fabriquant(self):

        client = APIClient()
        data = {
            'email': "admin@renault.com",
            'password' : "adminadmin",
            'nom' : "Hamza",
            'prenom' : "ZAIDI",
            'adresse' : "Bouchaoui",
            'tel' : "0561725710",
            'marque' : 1
        }

        response = client.post('/accounts/fabriquant',data)
        assert response.status_code == 201
        user = Fabriquant.objects.get(email = "admin@renault.com")
        assert user.is_admin_fabriquant

