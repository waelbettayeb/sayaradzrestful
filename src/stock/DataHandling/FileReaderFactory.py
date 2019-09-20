from stock.DataHandling.CSVFileReader import CsvFileReader

class FileReaderFactory():
    def create_file_reader(self, **kwargs):
        if 'type' not in kwargs.keys():
            return CsvFileReader()
        if kwargs['type'] != 'csv':
            if 'delimiter' in kwargs.keys():
                raise ValueError('Delimiter should only be used with csv files.')
        if kwargs['type'] == 'csv':
            if 'delimiter' in kwargs.keys():
                return CsvFileReader(delimiter= kwargs['delimiter'])
