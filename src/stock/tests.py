import io

import os

from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from couleur.models import Couleur
from marque.models import Marque
from modele.models import Modele
from option.models import Option
from reservation.models import Vehicule
from version.models import Version
from accounts.models import Fabriquant


class TestStockFileUpload(APITestCase):

    def setUp(self):

        renault = self.insert_marque('R1','Renault')
        symbole = self.insert_model('M1',renault,'Symbole')

        self.insert_color(21561)
        self.insert_color(32184)

        self.insert_version(32165,symbole)
        self.insert_version(65811, symbole)

        self.insert_option(1822)
        self.insert_option(3214)
        self.insert_option(32188)
        self.insert_option(321842)
        self.insert_option(654321)
        self.insert_option(654218)

        admin_renault = Fabriquant.objects.create_superuser("admin@renault.dz",
                                                            password="testpassword",
                                                            nom="Zaidi",
                                                            prenom="Hamza",
                                                            adresse="Bouchaoui",
                                                            tel="023228511",
                                                            marque=renault
                                                            )


        pass

    def insert_color(self, Code_Couleur):
        couleur = Couleur(Code_Couleur=Code_Couleur)
        couleur.save()

        pass

    def insert_version(self, Code_Version, Modele):
        version = Version(Code_Version = Code_Version, Id_Modele= Modele)
        version.save()
        pass

    def insert_option(self, Code_option):
        option = Option(Code_Option= Code_option)
        option.save()
        pass

    def insert_model(self, Id_Modele,marque,nom):
        modele = Modele.objects.create(Code_Modele= Id_Modele, Id_Marque= marque, Nom_Modele= nom)
        return modele

    def insert_marque(self, Id_Marque, Nom_Marque):
        marque = Marque.objects.create(Id_Marque = Id_Marque, Nom_Marque =  Nom_Marque)
        marque.save()
        return marque




    def test_upload_file(self):


        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'DataHandling/test.csv')
        with io.open(file_path,encoding='utf-8') as stock_file:
            print(stock_file.encoding)
            client = APIClient()
            client.force_authenticate(user= Fabriquant.objects.get(email= 'admin@renault.dz'))
            data = {
                'file' :stock_file
            }

            response = client.post(path='/stock/upload' , data= data)
            print(response.data)
            assert Vehicule.objects.filter(Numero_Chassis='FAS131').exists()