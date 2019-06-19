from django.test import TestCase

from couleur.models import Couleur
from marque.models import Marque
from modele.models import Modele
from option.models import Option
from reservation.models import Vehicule
from stock.DataHandling.CSVFileReader import CsvFileReader
from stock.DataHandling.DataHandler import DataHandler
from version.models import Version


class ReadingDataTestCase(TestCase):



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


    def test_valid_csv_file_reading(self):
        file_reader = CsvFileReader(delimiter=',')
        data = file_reader.get_file_data('test.csv')
        assert data['clean']
        assert len(data['data']) == 2

        pass

    def test_invalid_csv_file_reading(self):
        file_reader = CsvFileReader(delimiter=',')
        data = file_reader.get_file_data('invalid_test.csv')
        assert not data['clean']
        assert len(data['errors']) == 1
        pass

    def test_data_insertion(self):

        data_handler = DataHandler()
        data_handler.handle_data('test.csv')

        assert Vehicule.objects.filter(Numero_Chassis='FAS131').exists()
        assert Vehicule.objects.filter(Numero_Chassis='ASQDQF').exists()

        vehicule = Vehicule.objects.get(Numero_Chassis='FAS131')
        assert len(vehicule.Liste_Option.all()) == 3

        vehicule = Vehicule.objects.get(Numero_Chassis='ASQDQF')
        assert len(vehicule.Liste_Option.all()) == 2