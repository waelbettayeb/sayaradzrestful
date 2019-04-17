from stock.DataHandling.FileValidityChecker import FileValidityChecker

class CsvFileValidityChecker(FileValidityChecker):

    def check_validity(self, file):
        errors = []


        if not 'numero_chassis' in file.fieldnames:
            errors.append('Le fichier doit contenir le numeor de chassis')

        if not 'concessionaire' in file.fieldnames :
            errors.append('Le fichier doit contenir le concessionaire')

        if not 'code_couleur' in file.fieldnames:
            errors.append('Le fichier doit contenir le code de couleur')

        if not 'code_version' in file.fieldnames:
            errors.append('Le fichier doit contenir le code de version')


        return errors