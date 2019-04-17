from stock.DataHandling.CSVFileValidityChecker import CsvFileValidityChecker
from stock.DataHandling.FileReader import FileReader
import csv

class CsvFileReader(FileReader):

    def __init__(self, delimiter, file_validator):
        super().__init__(file_validator)
        self.file_validator = CsvFileValidityChecker()
        self.delimiter = delimiter

    def get_file_data(self, file_path):
        data = []
        with open(file_path) as stock_file:
            csv_reader = csv.reader(stock_file,delimiter = self.delimiter)
            errors = self.file_validator.check_validity(csv_reader)
            if len(errors) != 0:
                return errors
            for row in csv_reader:
                vehicule = {}
                vehicule['numero_chassis'] = row[0]
                vehicule['concessionaire'] = row[1]
                vehicule['code_couleur'] = row[2]
                vehicule['code_version'] = row[3]

        return data