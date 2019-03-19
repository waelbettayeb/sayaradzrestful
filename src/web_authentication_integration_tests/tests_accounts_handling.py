from oauth2_provider.models import Application
from rest_framework.test import APITestCase, APIClient

import accounts.models as accounts
from marque.models import Marque


def create_authentication_data(email, password):
    admin = accounts.Administrateur.objects.get(email='admin@sayara.dz')

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

    return data

def create_marque(Id_marque, Nom_Marque):
    created_marque = Marque.objects.create(Id_Marque=Id_marque, Nom_Marque=Nom_Marque)
    created_marque.save()
    return created_marque


def create_utlisateur_fabriquant(email, password,nom,prenom,adresse,tel ,marque):

    user = accounts.Fabriquant.objects.create_user(email,
                                         password=password,
                                         nom=nom,
                                         prenom=prenom,
                                         adresse=adresse,
                                         tel=tel,
                                         marque=marque
    )
    user.save()


def create_admin_fabriquant(email, password, nom, prenom, adresse, tel, id_marque, nom_marque):

    marque = create_marque(id_marque,nom_marque)
    user = accounts.Fabriquant.objects.create_user(email,
                                                   password=password,
                                                   nom=nom,
                                                   prenom=prenom,
                                                   adresse=adresse,
                                                   tel=tel,
                                                   marque=marque
                                                   )
    user.save()

    return user


def create_authentication_header(token):
    return "Bearer {}".format(token)



class AdminstrateurTestCase(APITestCase):
    def setUp(self):
        admin = accounts.Administrateur.objects.create(email = 'admin@sayara.dz', password = 'adminadmin')
        admin.save()


