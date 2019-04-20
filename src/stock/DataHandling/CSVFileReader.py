from stock.DataHandling.CSVFileValidityChecker import CsvFileValidityChecker
from stock.DataHandling.FileReader import FileReader
import csv


class CsvFileReader(FileReader):

    def __init__(self, delimiter):
        self.file_validator = CsvFileValidityChecker()
        self.delimiter = delimiter

    def __get_options(self, row):
        indexes = range(len(row) - 4)
        options = []
        for i in indexes:
            index = 'option_{}'.format(i)
            options.append(row[index])

        return options

    def get_file_data(self, file_path):
        data = []
        response = {}
        response['clean'] = True
        with open(file_path) as stock_file:
            csv_reader = csv.reader(stock_file,delimiter = self.delimiter)
            errors = self.file_validator.check_validity(csv_reader)
            if len(errors) != 0:
                response['clean'] = False
                response['errors'] = errors
            else :
                for row in csv_reader:
                    vehicule = {}
                    vehicule['numero_chassis'] = row['numero_chassis']
                    vehicule['concessionaire'] = row['concessionaire']
                    vehicule['code_couleur'] = row['code_couleur']
                    vehicule['code_version'] = row['code_version']
                    vehicule['options'] = self.__get_options(row)
                    data.append(vehicule)
                response['data'] = data
            return response