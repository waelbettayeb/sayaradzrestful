from stock.DataHandling.CSVFileReader import CsvFileReader

class FileReaderFactory():
    def create_file_reader(self, **kwargs):
        if not kwargs['type']:
            return CsvFileReader()
        if kwargs['type'] != 'csv':
            if kwargs['delimiter']:
                raise ValueError('Delimiter should only be used with csv files.')
        if kwargs['type'] == 'csv':
            if kwargs['delimiter']:
                return CsvFileReader(delimiter= kwargs['delimiter'])
