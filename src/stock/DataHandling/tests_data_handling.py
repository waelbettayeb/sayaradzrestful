from django.test import TestCase

from stock.DataHandling.CSVFileReader import CsvFileReader


class ReadingDataTestCase(TestCase):



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



    pass