from django.forms.models import model_to_dict
from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient, APIRequestFactory, force_authenticate

from accounts.models import Fabriquant, Administrateur, User
from accounts.serializers import UtilisateurFabriquantSerializer
from . import views
from marque.models import Marque
from . import urls
from oauth2_provider.models import *


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
        user = User.objects.get(email="admin@renault.dz")
        client.force_authenticate(user=user)
        response = client.get('/accounts/fabriquant/utlisateur/1')
        assert response.status_code == 200
        assert len(response.data) == 2
        user1 = Fabriquant.objects.get(email="user1@renault.dz")
        serializer = UtilisateurFabriquantSerializer(user1)
        assert serializer.data in response.data

    def test_list_utilisateurs_fabriquant_admin(self):
        admin = Administrateur.objects.create_superuser(
            email="admin@sayara.dz",
            password="adminadmin"
        )
        admin.save()
        admin = User.objects.get(email= "admin@sayara.dz")
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
        assert response.status_code == 401

    def test_fail_list_fabriquant_not_allowed(self):
        client = APIClient()
        user = User.objects.get(email="admin@renault.dz")
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
            #'marque': 1
        }
        response = client.post('/accounts/fabriquant/utilisateur', data)
        self.assertEqual(str(response.data['detail']), "Authentication credentials were not provided.")
        assert response.status_code == 401

    def test_fail_create_utilisateur_by_non_admin(self):
        client = APIClient()
        user = User.objects.get(email="user1@renault.dz")
        client.force_authenticate(user=user)
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "Nom user2",
            'prenom': "user2",
            'adresse': "Adresse user2",
            'tel': "0265884135",
        }
        response = client.post('/accounts/fabriquant/utilisateur', data)
        self.assertEqual(str(response.data['detail']), "You do not have permission to perform this action.")
        assert response.status_code == 403

    def test_create_utilisateur_fabriquant_by_admin_fabriquat(self):
        client = APIClient()
        admin_renault = User.objects.get(email="admin@renault.dz")
        client.force_authenticate(user=admin_renault)
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "Nom user2",
            'prenom': "user2",
            'adresse': "Adresse user2",
            'tel': "0265884135",
        }
        try:
            user = Fabriquant.objects.get(email="user2@renault.dz")
        except:
            user = None
        assert user == None
        response = client.post('/accounts/fabriquant/utilisateur', data)
        assert response.status_code == 201
        expected_user = Fabriquant.objects.get(email="user2@renault.dz")
        assert expected_user != None

    def test_create_utilisateur_fabriquant_by_admin(self):

        admin = Administrateur.objects.create_superuser(
            email="admin@sayara.dz",
            password="adminadmin"
        )
        admin.save()
        admin = User.objects.get(email = "admin@sayara.dz")
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
        response = client.post('/accounts/fabriquant/utilisateur', data)
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
        user_renault = Fabriquant.objects.create_user("user2@renault.dz",
                                                      password="testpassword",
                                                      nom="Zaidi2",
                                                      prenom="Hamza2",
                                                      adresse="Bouchaoui2",
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
        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz', password='adminadmin')
        admin.save()
        admin = User.objects.get(email= 'admin@sayara.dz')
        client = APIClient()
        client.force_authenticate(user=admin)
        data = {
            'email': "user1@renault.dz",
            'password': "123456235",
            'nom': "ZAIDI",
            'prenom': "Hamza",
            'adresse': "Adresse updated",
            'tel': "0265884135",
        }
        response = client.put('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert response.status_code == 200
        assert expected_user.adresse == "Adresse updated"

    def test_update_utilisateur_by_admin_fabriquant(self):
        admin_fabriquant = User.objects.get(email='admin@renault.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        data = {
            'email': "user1@renault.dz",
            'password': "123456235",
            'nom': "ZAIDI",
            'prenom': "Hamza",
            'adresse': "Adresse updated",
            'tel': "0265884135",
        }
        response = client.put('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert response.status_code == 200
        assert expected_user.adresse == "Adresse updated"

    def test_fail_update_utilisateur_by_non_owner(self):
        admin_fabriquant = User.objects.get(email='admin@peugeot.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        user = Fabriquant.objects.get(email='user1@renault.dz')
        old_adresse = user.adresse
        data = {
            'email': "user1@renault.dz",
            'password': "123456235",
            'nom': "ZAIDI",
            'prenom': "Hamza",
            'adresse': "Adresse updated2",
            'tel': "0265884135",
        }
        response = client.put('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        assert response.status_code == 403
        user = Fabriquant.objects.get(email='user1@renault.dz')
        assert user.adresse == old_adresse

    def test_fail_update_utilisateur_by_non_other_users(self):
        user = User.objects.get(email='user1@renault.dz')
        client = APIClient()
        client.force_authenticate(user=user)
        user = Fabriquant.objects.get(email='user2@renault.dz')
        old_adresse = user.adresse
        data = {
            'email': "user2@renault.dz",
            'password': "123456235",
            'nom': "ZAIDI",
            'prenom': "Hamza",
            'adresse': "Adresse updated2",
            'tel': "0265884135",
        }
        response = client.put('/accounts/fabriquant/utilisateur/user2@renault.dz', data)
        assert response.status_code == 403
        user = Fabriquant.objects.get(email='user2@renault.dz')
        assert user.adresse == old_adresse

    def test_utilisateur_fabriquant_can_update_his_own(self):
        admin_fabriquant = User.objects.get(email='user1@renault.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        data = {
            'email': "user1@renault.dz",
            'password': "123456235",
            'nom': "ZAIDI",
            'prenom': "Hamza",
            'adresse': "Adresse updated",
            'tel': "0265884135",
        }
        response = client.put('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert response.status_code == 200
        assert expected_user.adresse == "Adresse updated"


    def test_admin_can_decativate_user(self):
        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz', password='adminadmin')
        admin.save()
        admin = User.objects.get(email='admin@sayara.dz')
        client = APIClient()
        client.force_authenticate(user=admin)
        data = {
            'is_active' : False,
            'adresse' : 'Update'
        }
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert expected_user.is_active == True
        response = client.patch('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert response.status_code == 200
        assert expected_user.is_active == False

    def test_admin_fabriquant_can_deactivate_own_user(self):
        admin_fabriquant = User.objects.get(email='admin@renault.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        data = {
            'is_active': False,
            'adresse': 'Update'
        }
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert expected_user.is_active == True
        response = client.patch('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert response.status_code == 200
        assert expected_user.is_active == False

    def test_admin_fabriquant_cannot_deactivate_self(self):
        admin_fabriquant = User.objects.get(email='admin@renault.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        data = {
            'is_active': False,
            'adresse': 'Update'
        }
        user = Fabriquant.objects.get(email='admin@renault.dz')
        assert user.is_active == True
        response = client.patch('/accounts/fabriquant/utilisateur/admin@renault.dz', data)
        assert response.status_code == 403
        user = Fabriquant.objects.get(email = 'admin@renault.dz')
        assert user.is_active == True

    def test_users_cannot_deactivate_self(self):
        admin_fabriquant = User.objects.get(email='user1@renault.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        data = {
            'is_active': False,
            'adresse': 'Update'
        }
        user = Fabriquant.objects.get(email='admin@renault.dz')
        assert user.is_active == True
        response = client.patch('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        assert response.status_code == 403
        user = Fabriquant.objects.get(email = 'admin@renault.dz')
        assert user.is_active == True

    def test_other_maruque_cannot_deactivate_user(self):
        admin_fabriquant = User.objects.get(email='admin@peugeot.dz')
        client = APIClient()
        client.force_authenticate(user=admin_fabriquant)
        data = {
            'is_active': False,
            'adresse': 'Update'
        }
        user = Fabriquant.objects.get(email='admin@renault.dz')
        assert user.is_active == True
        response = client.patch('/accounts/fabriquant/utilisateur/user1@renault.dz', data)
        assert response.status_code == 403
        user = Fabriquant.objects.get(email='admin@renault.dz')
        assert user.is_active == True


class RetrieveUtilisateursFabriquantTestCases(APITestCase):

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
        user_renault = Fabriquant.objects.create_user("user2@renault.dz",
                                                      password="testpassword",
                                                      nom="Zaidi2",
                                                      prenom="Hamza2",
                                                      adresse="Bouchaoui2",
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

        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz', password='adminadmin')
        admin.save()

    def retrieve_user(self,user,email):
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/accounts/fabriquant/utilisateur/{}'.format(email))
        return response

    def test_admin_can_retreive_utilisateur_fabriquant(self):
        admin = User.objects.get(email='admin@sayara.dz')
        response = self.retrieve_user(admin,'user1@renault.dz')
        assert response.status_code == 200
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        serializer = UtilisateurFabriquantSerializer(expected_user)
        assert serializer.data == response.data


    def test_admin_fabriquant_can_retreive_own_utilisateur(self):

        admin_fabriquant = User.objects.get(email='admin@renault.dz')
        response = self.retrieve_user(admin_fabriquant,'user1@renault.dz')
        assert response.status_code == 200
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        serializer = UtilisateurFabriquantSerializer(expected_user)
        assert serializer.data == response.data


    def test_utilisateur_can_retrieve_own(self):
        user1_renault = User.objects.get(email='user1@renault.dz')
        response = self.retrieve_user(user1_renault, 'user1@renault.dz')
        assert response.status_code == 200
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        serializer = UtilisateurFabriquantSerializer(expected_user)
        assert serializer.data == response.data

    def test_fail_retrieve_utilisateur_by_other_marque(self):
        admin_peugeot = User.objects.get(email='admin@peugeot.dz')
        response = self.retrieve_user(admin_peugeot,'user1@renault.dz')
        assert response.status_code == 403


class DeleteUtilisateurFabriquantTestCases(APITestCase):

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
        user_renault = Fabriquant.objects.create_user("user2@renault.dz",
                                                      password="testpassword",
                                                      nom="Zaidi2",
                                                      prenom="Hamza2",
                                                      adresse="Bouchaoui2",
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

        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz', password='adminadmin')
        admin.save()

    def delete_user(self,user,email):
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.delete('/accounts/fabriquant/utilisateur/{}'.format(email))
        return response

    def test_admin_delete_utilisatuer_fabriquant(self):

        admin = User.objects.get(email='admin@sayara.dz')
        response = self.delete_user(admin,'user1@renault.dz')
        assert response.status_code == 204
        try:
            Fabriquant.objects.get(email='user1@renault.dz')
        except:
            assert True

    def test_admin_can_delete_admin_fabriquant(self):
        admin = User.objects.get(email='admin@sayara.dz')
        response = self.delete_user(admin, 'admin@renault.dz')
        assert response.status_code == 204
        try:
            Fabriquant.objects.get(email='admin@renault.dz')
        except:
            assert True

    def test_admin_fabriquant_can_delte_own_utlisateur_fabriquant(self):
        admin_renault = User.objects.get(email='admin@renault.dz')
        response = self.delete_user(admin_renault, 'user1@renault.dz')
        assert response.status_code == 204
        try:
            Fabriquant.objects.get(email='user1@renault.dz')
        except:
            assert True


    def test_fail_delete_by_other_marque(self):
        admin_renault = User.objects.get(email='admin@renault.dz')
        response = self.delete_user(admin_renault, 'user1@peugeot.dz')
        assert response.status_code == 403
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert expected_user != None

    def test_fail_delete_own_account(self):
        user = User.objects.get(email='user1@peugeot.dz')
        response = self.delete_user(user, 'user1@peugeot.dz')
        assert response.status_code == 403
        expected_user = Fabriquant.objects.get(email='user1@renault.dz')
        assert expected_user != None

        pass


class CreateAdminFabriquantTestCases(APITestCase):

    def setUp(self):
        renault = Marque.objects.create(Id_Marque=1, Nom_Marque='Renault')
        renault.save()

        admin_renault = Fabriquant.objects.create_superuser("admin@renault.dz",
                                                            password="testpassword",
                                                            nom="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel="023228511",
                                                            marque=renault
                                                            )
        admin_renault.save()

        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz',password='adminadmin')
        admin.save()

    def create_marque(self, Id_Marque, Nom_Marque):
        try:
            marque = Marque.objects.create(Id_Marque=Id_Marque, Nom_Marque="BMW")
            marque.save()
        except:
            raise ValueError('Cette marque existe déja')


    def create_admin_fabriquant(self,user,email,Id_Marque):
        client = APIClient()
        if user != None:
            client.force_authenticate(user=user)
        data = {
            'email': email,
            'password': "adminadmin",
            'nom': "Nom admin Bmw",
            'prenom': "Prenom admin Bmw",
            'adresse': "Adresse admin Bmw",
            'tel': "0265884135",
            'marque': Id_Marque
        }
        response = client.post('/accounts/fabriquant', data)
        return response


    def test_register_admin_fabriquant(self):
        email = "admin@bmw.dz"
        Id_Marque = 3
        self.create_marque(Id_Marque, "BMW")
        user = None
        response = self.create_admin_fabriquant(user,email= email,Id_Marque= Id_Marque)
        assert response.status_code == 201
        created_user = Fabriquant.objects.get(email = email)
        serializer = UtilisateurFabriquantSerializer(created_user)
        assert serializer.data == response.data
        assert created_user.is_admin_fabriquant


    def test_create_amdin_fabriquant_by_admin(self):
        email = "admin@bmw.dz"
        Id_Marque = 3
        self.create_marque(Id_Marque,"BMW")
        admin = User.objects.get(email='admin@sayara.dz')
        response = self.create_admin_fabriquant(admin, email, Id_Marque)
        assert response.status_code == 201
        created_user = Fabriquant.objects.get(email=email)
        serializer = UtilisateurFabriquantSerializer(created_user)
        assert serializer.data == response.data
        assert created_user.is_admin_fabriquant

    def test_fail_create_second_admin_by_anonymos(self):
        email = "admin2@renault.dz"
        Id_Marque = 1
        user = None
        response = self.create_admin_fabriquant(user, email=email, Id_Marque=Id_Marque)
        assert response.status_code == 401
        try:
            Fabriquant.objects.get(email="admin2@renault.dz")
        except:
            assert True


class WebAuthenticationTestCases(APITestCase):

    def authenticate_user(self, email, password):
        admin = Administrateur.objects.create_superuser(email='admin@sayara.dz', password='adminadmin')
        admin.save()

        app = Application.objects.create(
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD,
            name='SayaraDZWeb',
            user=admin
        )

        data = {
            'grant_type': "password",
            'username': email,
            'password': password,
            'client_id': app.client_id,
            'client_secret': app.client_secret
        }

        client = APIClient()
        response = client.post('/accounts/token', data)
        return response



    def create_utlisateur_fabriquant(self, email, password, marque):
        created_marque = Marque.objects.create(Id_Marque=marque, Nom_Marque='Renault')
        created_marque.save()

        user = Fabriquant.objects.create_user(email,
                                                      password=password,
                                                      nom="Zaidi",
                                                      prenom="Hamza",
                                                      adresse="Bouchaoui",
                                                      tel="023228511",
                                                      marque=created_marque
                                                      )
        user.save()

    def create_admin_fabriquant(self, email, password, marque):
        created_marque = Marque.objects.create(Id_Marque=marque, Nom_Marque='Renault')
        created_marque.save()

        user = Fabriquant.objects.create_superuser(email,
                                              password=password,
                                              nom="Zaidi",
                                              prenom="Hamza",
                                              adresse="Bouchaoui",
                                              tel="023228511",
                                              marque=created_marque
                                              )
        user.save()

    def create_authentication_header(self, token):
        return "Bearer {}".format(token)

    def test_admin_authentication(self):

        response = self.authenticate_user('admin@sayara.dz','adminadmin')
        assert response.status_code == 200
        access_token = response.data['access_token']
        user = AccessToken.objects.get(token = access_token).user
        assert user.is_admin
        assert user.is_admin_fabriquant == False
        assert user.is_fabriquant == False
        assert user.is_automobiliste == False

    def test_admin_fabriquant_authentication(self):
        self.create_admin_fabriquant('admin@renault.dz','password',1)
        response = self.authenticate_user('admin@renault.dz', 'password')

        assert response.status_code == 200
        access_token = response.data['access_token']
        user = AccessToken.objects.get(token= access_token).user
        assert user.is_admin == False
        assert user.is_admin_fabriquant
        assert user.is_fabriquant
        assert user.is_automobiliste == False
        admin_fabriquant = Fabriquant.objects.get(email = user.email)
        assert admin_fabriquant.marque.Id_Marque == str(1)

    def test_utilisatuer_fabriquant_authentication(self):
        self.create_utlisateur_fabriquant('admin@renault.dz', 'password', 1)
        response = self.authenticate_user('admin@renault.dz', 'password')

        assert response.status_code == 200
        access_token = response.data['access_token']
        user = AccessToken.objects.get(token=access_token).user
        assert user.is_admin == False
        assert user.is_admin_fabriquant == False
        assert user.is_fabriquant
        assert user.is_automobiliste == False
        admin_fabriquant = Fabriquant.objects.get(email=user.email)
        assert admin_fabriquant.marque.Id_Marque == str(1)

    def test_fail_get_access_token_for_invalid_credentials(self):
        response = self.authenticate_user('admin@renault.dz', 'password')
        assert response.status_code == 400
        expected_error = {
                        'error_description' :'Invalid credentials given.',
                        'error': 'invalid_grant'
        }
        self.assertEqual(response.data ,expected_error )


