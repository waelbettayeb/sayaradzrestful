from django.forms.models import model_to_dict
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient, APIRequestFactory, force_authenticate

from accounts.models import Fabriquant, Administrateur
from accounts.serializers import FabriquantSerializer
from . import views
from marque.models import Marque
from . import urls



class ListFabriquantTestCases(APITestCase):


    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        peugeot = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeot.save()

        admin_renault = Fabriquant.objects.create_superuser("admin@renault.dz",
                                                           password="testpassword",
                                                           nom="Zaidi",
                                                           prenom="Hamza",
                                                           adresse="Bouchaoui",
                                                           tel="023228511",
                                                           marque=renault
                                                           )
        admin_renault.save()

        user_renault = Fabriquant.objects.create_user("user1@renault.dz",
                                                           password="testpassword",
                                                           nom="Zaidi",
                                                           prenom="Hamza",
                                                           adresse="Bouchaoui",
                                                           tel="023228511",
                                                           marque=renault
                                                           )
        user_renault.save()

        admin_peugeot = Fabriquant.objects.create_superuser("admin@peugeot.dz",
                                                            password="testpassword",
                                                            nom="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel="023228511",
                                                            marque=peugeot
                                                            )
        admin_peugeot.save()

        user_peugeot = Fabriquant.objects.create_user("user1@peugeot.dz",
                                                      password="testpassword",
                                                      nom="Zaidi",
                                                      prenom="Hamza",
                                                      adresse="Bouchaoui",
                                                      tel="023228511",
                                                      marque=peugeot
                                                      )
        user_peugeot.save()


    def test_list_utilisateurs_fabriquant_admin_fabriquant(self):
        # Check if there are nor errors while rquesting the view
        client = APIClient()
        user = Fabriquant.objects.get(email = "admin@renault.dz")
        client.force_authenticate(user = user)
        response =  client.get('/accounts/fabriquant/utlisateur/1')
        assert response.status_code == 200
        assert len(response.data) == 2
        user1 = Fabriquant.objects.get(email="user1@renault.dz")
        serializer = FabriquantSerializer(user1)
        assert serializer.data in response.data


    def test_list_utilisateurs_fabriquant_admin(self):
        admin = Administrateur.objects.create_superuser(
            email= "admin@sayara.dz",
            password= "adminadmin"
        )
        client = APIClient()
        client.force_authenticate(user=admin)
        response = client.get('/accounts/fabriquant/utlisateur/1')
        assert response.status_code == 200
        assert len(response.data) == 2
        response = client.get('/accounts/fabriquant/utlisateur/2')
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_fail_list_fabriquant_not_authenticated(self):
        # Check if there are nor errors while rquesting the view
        client = APIClient()
        response = client.get('/accounts/fabriquant/utlisateur/1')
        self.assertEqual(str(response.data['detail']), "Authentication credentials were not provided.")
        assert response.status_code == 403

    def test_fail_list_fabriquant_not_allowed(self):
        client = APIClient()
        user = Fabriquant.objects.get(email="admin@renault.dz")
        client.force_authenticate(user=user)
        response = client.get('/accounts/fabriquant/utlisateur/2')
        assert response.status_code == 403


class CreateUtilisateurFabriquantTestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        peugeot = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeot.save()

        admin_renault = Fabriquant.objects.create_superuser("admin@renault.dz",
                                                           password="testpassword",
                                                           nom="Zaidi",
                                                           prenom="Hamza",
                                                           adresse="Bouchaoui",
                                                           tel="023228511",
                                                           marque=renault
                                                           )
        admin_renault.save()

        user_renault = Fabriquant.objects.create_user("user1@renault.dz",
                                                           password="testpassword",
                                                           nom="Zaidi",
                                                           prenom="Hamza",
                                                           adresse="Bouchaoui",
                                                           tel="023228511",
                                                           marque=renault
                                                           )
        user_renault.save()

        admin_peugeot = Fabriquant.objects.create_superuser("admin@peugeot.dz",
                                                            password="testpassword",
                                                            nom="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel="023228511",
                                                            marque=peugeot
                                                            )
        admin_peugeot.save()

        user_peugeot = Fabriquant.objects.create_user("user1@peugeot.dz",
                                                      password="testpassword",
                                                      nom="Zaidi",
                                                      prenom="Hamza",
                                                      adresse="Bouchaoui",
                                                      tel="023228511",
                                                      marque=peugeot
                                                      )
        user_peugeot.save()


    def test_fail_crete_utilisateur_fabriquant_not_authenticated(self):
        client = APIClient()
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "Nom user2",
            'prenom': "user2",
            'adresse': "Adresse user2",
            'tel': "0265884135",
            'marque': 1
        }
        response = client.post('/accounts/fabriquant/utilisateur', data)
        self.assertEqual(str(response.data['detail']), "Authentication credentials were not provided.")
        assert response.status_code == 403


    def test_fail_create_utilisateur_fabriquant_by_not_owner(self):
        client = APIClient()
        user = Fabriquant.objects.get(email="admin@renault.dz")
        client.force_authenticate(user=user)
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "Nom user2",
            'prenom': "user2",
            'adresse': "Adresse user2",
            'tel': "0265884135",
            'marque': 2
        }
        response = client.post('/accounts/fabriquant/utilisateur', data)
        self.assertEqual(str(response.data['detail']), "You do not have permission to perform this action.")
        assert response.status_code == 403

    def test_fail_create_utilisateur_by_non_admin(self):
        client = APIClient()
        user = Fabriquant.objects.get(email="user1@renault.dz")
        client.force_authenticate(user=user)
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "Nom user2",
            'prenom': "user2",
            'adresse': "Adresse user2",
            'tel': "0265884135",
            'marque': 1
        }
        response = client.post('/accounts/fabriquant/utilisateur', data)
        self.assertEqual(str(response.data['detail']), "You do not have permission to perform this action.")
        assert response.status_code == 403

    def test_create_utilisateur_fabriquant_by_admin_fabriquat(self):
        client = APIClient()
        admin_renault = Fabriquant.objects.get(email="admin@renault.dz")
        client.force_authenticate(user=admin_renault)
        data = {
            'email' : "user2@renault.dz",
            'password' : "123456235",
            'nom' : "Nom user2",
            'prenom' : "user2",
            'adresse' : "Adresse user2",
            'tel' : "0265884135",
            'marque' : 1
        }
        try:
           user = Fabriquant.objects.get(email = "user2@renault.dz")
        except:
            user = None
        assert user == None
        response = client.post('/accounts/fabriquant/utilisateur', data)
        assert response.status_code == 201
        expected_user = Fabriquant.objects.get(email = "user2@renault.dz")
        assert expected_user  != None


    def test_create_utilisateur_fabriquant_by_admin(self):

        admin = Administrateur.objects.create_superuser(
            email="admin@sayara.dz",
            password="adminadmin"
        )
        client = APIClient()
        client.force_authenticate(user=admin)
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "Nom user2",
            'prenom': "user2",
            'adresse': "Adresse user2",
            'tel': "0265884135",
            'marque': 1
        }
        response = client.post('/accounts/fabriquant/utilisateur',data)
        print(response.data)
        assert response.status_code == 201

class UpdateUtilisateurFabriquantTestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        peugeot = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeot.save()

        admin_renault = Fabriquant.objects.create_superuser("admin@renault.dz",
                                                           password="testpassword",
                                                           nom="Zaidi",
                                                           prenom="Hamza",
                                                           adresse="Bouchaoui",
                                                           tel="023228511",
                                                           marque=renault
                                                           )
        admin_renault.save()

        user_renault = Fabriquant.objects.create_user("user1@renault.dz",
                                                           password="testpassword",
                                                           nom="Zaidi",
                                                           prenom="Hamza",
                                                           adresse="Bouchaoui",
                                                           tel="023228511",
                                                           marque=renault
                                                           )
        user_renault.save()

        admin_peugeot = Fabriquant.objects.create_superuser("admin@peugeot.dz",
                                                            password="testpassword",
                                                            nom="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel="023228511",
                                                            marque=peugeot
                                                            )
        admin_peugeot.save()

        user_peugeot = Fabriquant.objects.create_user("user1@peugeot.dz",
                                                      password="testpassword",
                                                      nom="Zaidi",
                                                      prenom="Hamza",
                                                      adresse="Bouchaoui",
                                                      tel="023228511",
                                                      marque=peugeot
                                                      )
        user_peugeot.save()

    def test_update_utilisateur_by_admin(self):
        #TODO implement
        pass

    def test_update_utilisateur_by_admin_fabriquant(self):
        #TODO implement
        pass

    def test_fail_update_utilisateur_by_non_owner(self):
        pass

    def test_fail_update_utilisateur_by_non_woner(self):
        pass


    pass




class CreateAdminFabriquantTestCases(APITestCase):



    def test_register_admin_fabriquant(self):
        client = APIClient()
        BMW = Marque.objects.create(Id_Marque = 3, Nom_Marque = "BMW")
        BMW.save()

        data = {
            'email' : "admin@bmw.dz",
            'password' :"adminadmin",
            'nom': "Nom admin Bmw",
            'prenom': "Prenom admin Bmw",
            'adresse': "Adresse admin Bmw",
            'tel': "0265884135",
            'marque': 3
        }
        response = client.post('/accounts/fabriquant',data)
        assert response.status_code == 201


    def test_create_amdin_fabriquant_by_admin(self):
        client = APIClient()
        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz', password = 'adminadmin')
        client.force_authenticate(user=admin)
        BMW = Marque.objects.create(Id_Marque=3, Nom_Marque="BMW")
        BMW.save()

        data = {
            'email': "admin@bmw.dz",
            'password': "adminadmin",
            'nom': "Nom admin Bmw",
            'prenom': "Prenom admin Bmw",
            'adresse': "Adresse admin Bmw",
            'tel': "0265884135",
            'marque': 3
        }
        response = client.post('/accounts/fabriquant', data)
        assert response.status_code == 201


    def test_fail_create_second_admin_by_anonymos(self):
        #TODO
        pass



class FabriquantTestCases(APITestCase):
    first_len = 0

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()
        peugeot = Marque.objects.create(Id_Marque=2, Nom_Marque='Peugeot')
        peugeot.save()

        fabriquant_1 = Fabriquant.objects.create_superuser("fk_zaidi@esi.dz",
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





    def test_fail_list_fabriquant(self):

        """ Get Request to list Utilisateurs Fabriquant should return Forbidden
            if the user isn't authenticated or isn't an admin or isn't an admin_fabriquant
        """
        factory = APIRequestFactory()
        request = factory.get('/accounts/fabriquant/utilisateur')
        view = FabriquantView.as_view()
        response = view(request)
        assert response.status_code == 403 # Forbidden because the user is not authenticated
        user = Fabriquant.objects.get(email="fk_zaidi_test@esi.dz")  # <-This user is not an admin_fabriquant
        force_authenticate(request, user=user)
        response = view(request)
        assert response.status_code == 403 # Forbiden because the user is not an admin_fabriquant

    def test_create_fabriquant(self):
        factory = APIRequestFactory()
        user = Fabriquant.objects.get(email="fk_zaidi@esi.dz")
        data = {
            'email' : "test@test.com",
            'password' : "test",
            'nom' : "Test",
            'prenom' :"Test",
            'adresse' : "Test",
            'tel' :"0561725710",
            'marque' : 2
        }
        request = factory.post('/accounts/fabriquant/utilisateur',data)
        force_authenticate(request, user=user)
        view = FabriquantView.as_view()
        response = view(request)
        #print(response.data)
        assert response.status_code == 201
        created_user = Fabriquant.objects.get(email = "test@test.com")
        assert not created_user == None
        renault_users = Fabriquant.objects.filter(marque = 1)
        assert not created_user in renault_users

    def test_fail_create_fabriquant(self):
        #TODO implement the test case
        pass

    def test_update_fabriquant(self):
        #TODO implement the test case
        pass

    def test_fail_update_fabriquant(self):
        #TODO implement the test case
        pass




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
        #print(response.data)
        assert response.status_code == 201
        user = Fabriquant.objects.get(email = "admin@renault.com")
        assert user.is_admin_fabriquant



