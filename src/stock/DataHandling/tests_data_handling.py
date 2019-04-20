from django.test import TestCase

from stock.DataHandling.CSVFileReader import CsvFileReader


class ReadingDataTestCase(TestCase):

    def test_valid_csv_file_reading(self):
        file_reader = CsvFileReader(delimiter=',')
        data = file_reader.get_file_data('test.csv')
        print(data)
        pass

    def test_invalid_csv_file_reading(self):
        pass

    pass