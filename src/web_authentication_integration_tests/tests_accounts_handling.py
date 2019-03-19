from oauth2_provider.models import Application
from rest_framework.test import APITestCase, APIClient

import accounts.models as accounts
from marque.models import Marque
from sayaradz import settings

CREATE_UTILISATUERS = '/accounts/fabriquant/utilisateur'
LIST_UTILISTATEURS  = '/accounts/fabriquant/utlisateur'
CREATE_ADMIN_FABRIQUANT = '/accounts/fabriquant'
RUD_UTILISATEUR_FABRIQUANT = '/accounts/fabriquant/utilisateur'

def create_oauth_application():
    admin = accounts.User.objects.get(email= 'admin@sayara.dz')
    app = Application.objects.create(
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_PASSWORD,
        name='SayaraDZWeb',
        user=admin
    )
    return app

def create_authentication_data(email, password, app):

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

def list_all_users_request(client, id_marque):

    response = client.get(LIST_UTILISTATEURS + '/{}'.format(id_marque))
    return response

def create_user(client, email, password,nom,prenom,adresse,tel , **kwargs) :
    data = {
        'email': email,
        'password': password,
        'nom': nom,
        'prenom': prenom,
        'adresse': adresse,
        'tel': tel,
    }
    if 'marque' in kwargs.keys():
        data['marque'] = kwargs['marque']

    response = client.post(CREATE_UTILISATUERS, data)
    return response

def create_admin_user(client, email, password,nom,prenom,adresse,tel ,marque):


    data = {
        'email' : email,
        'password' : password,
        'nom' : nom,
        'prenom' : prenom,
        'adresse' : adresse,
        'tel' : tel,
        'marque' : marque
    }

    response = client.post(CREATE_ADMIN_FABRIQUANT, data)
    return response


def retrieve_user(client, email):
    response = client.get(RUD_UTILISATEUR_FABRIQUANT +'/{}'.format(email))
    return response

def delete_user(client, email) :
    response = client.delete(RUD_UTILISATEUR_FABRIQUANT + '/{}'.format(email))
    return response

def update_user(client, email, new_data):
    response = client.patch(RUD_UTILISATEUR_FABRIQUANT + '/{}'.format(email), new_data)
    return response

def get_authentication_response(email,password, app):

    data = create_authentication_data(email=email, password=password, app=app)
    client = APIClient()
    authentication_response = client.post('/accounts/token', data)
    return authentication_response


def authenticate_client(authentication_response):
    client = APIClient()
    access_token = authentication_response.data['access_token']
    client.credentials(HTTP_AUTHORIZATION=create_authentication_header(access_token))
    return client

class AdminstrateurTestCase(APITestCase):
    def setUp(self):
        admin = accounts.Administrateur.objects.create_superuser(email = 'admin@sayara.dz', password = 'adminadmin')
        admin.save()

        admin_renault = create_admin_fabriquant(
            email='admin@renault.dz',
            password='password',
            nom= 'Admin',
            prenom='Renault',
            adresse='Cheraga',
            tel='023228511',
            id_marque=1,
            nom_marque='Renault'
        )
        create_utlisateur_fabriquant(
            email='user1@renault.dz',
            password='password',
            nom='User',
            prenom='Fabriquant',
            adresse='Cheraga',
            tel='023228511',
            marque= admin_renault.marque
        )

        admin_peugeot = create_admin_fabriquant(
            email='admin@peugeot.dz',
            password='password',
            nom='Admin',
            prenom='Peugeot',
            adresse='Cheraga',
            tel='023228511',
            id_marque=2,
            nom_marque='Peugeot'
        )
        create_utlisateur_fabriquant(
            email='user1@peugeot.dz',
            password='password',
            nom='User',
            prenom='Fabriquant',
            adresse='Cheraga',
            tel='023228511',
            marque=admin_peugeot.marque
        )

    def test_admin_operations(self):
        app = create_oauth_application()
        authentication_response = get_authentication_response('admin@sayara.dz','adminadmin',app)
        admin_client = authenticate_client(authentication_response)
        response = retrieve_user(admin_client,'user1@renault.dz')
        assert response.status_code == 200

        new_data = {
            'adresse' : 'New Address'
        }

        response = update_user(admin_client, 'user1@renault.dz', new_data)
        assert response.status_code == 200

        response = delete_user(admin_client, 'user1@renault.dz')
        assert response.status_code == 204

        # The deleted user shouldn't be able to login
        authentication_response = get_authentication_response('user1@renaul.dz','password',app)
        assert authentication_response.status_code == 400
        expected_response = {
            'error': 'invalid_grant',
            'error_description': 'Invalid credentials given.'
        }
        self.assertEqual(authentication_response.data,expected_response )
        response = create_user(
            admin_client,
            email='user3@renault.dz',
            password='password',
            nom='User3',
            prenom='User3',
            tel='023228511',
            adresse='Bab El Oued',
            marque = 1
        )

        assert response.status_code == 201

        # The created user should be able to login
        authentication_response = get_authentication_response('user3@renault.dz','password',app)
        assert authentication_response.status_code == 200

        # The created user should be able to see his own profile

        created_user_client = authenticate_client(authentication_response)
        response = retrieve_user(created_user_client, 'user3@renault.dz')
        assert response.status_code == 200

        response = list_all_users_request(admin_client, 1)
        assert response.status_code == 200
        create_marque(3, 'BMW')
        response = create_admin_user(
            admin_client,
            email= 'admin@bmw.dz',
            password='adminadmin',
            nom='BMW',
            prenom='BMW',
            adresse= 'Sovac',
            tel='0771442340',
            marque= 3
        )

        assert response.status_code == 201







