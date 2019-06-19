from couleur.models import Couleur
from option.models import Option
from reservation.models import Vehicule, List_Option
from stock.DataHandling.FileReaderFactory import FileReaderFactory
from version.models import Version


class DataHandler():

    def handle_data(self,file_path ,**kwargs):

        errors = None
        file_content = self.__read_file(file_path, **kwargs)
        if file_content['clean']:
            data = file_content['data']
            errors_details = []
            for vehicul in data :

                code_couleur = vehicul['code_couleur']
                code_version = vehicul['code_version']
                options = vehicul['options']
                error = {}
                color_exists, option_exists, version_exists = self.__check_existance(code_couleur,options, code_version)
                if color_exists and option_exists and version_exists :
                    vehicule = Vehicule(
                        Numero_Chassis= vehicul['numero_chassis'],
                        Concessionnaire= vehicul['concessionaire'],
                        Code_Version_id= vehicul['code_version'],
                        Code_Couleur_id= vehicul['code_couleur'])
                    vehicule.save()
                    for option in vehicul['options']:
                        option_obj = List_Option.objects.create(option = Option.objects.get(Code_Option=option), vehicule = vehicule)
                        option_obj.save()
                    vehicule.save()
                else :
                    error['numero_chassis'] = vehicul['numero_chassis']
                    if not color_exists :
                        error['code_couleur'] = vehicul['code_couleur']
                    if not code_version :
                        error['code_version'] = vehicul['code_version']
                    if not option_exists :
                        error['option'] = []
                        for option in options :
                            if not Option.objects.filter(Code_Option=option):
                                error['option'].append(option)
                    errors_details.append(error)

            if len(errors_details) != 0:
                errors = {}
                errors['type'] = "invalid data. some values don't exist in the data base"
                errors['details'] = errors_details
        else:
            errors = {}
            errors['type'] = 'file format is not valid.'
            errors['details'] = file_content['errors']
        return errors




    def __check_existance(self,Code_Couleur, options, Code_Version):
        option_exists = True
        color_exists = Couleur.objects.filter(Code_Couleur= Code_Couleur).exists()
        for option in options :
            if  not Option.objects.filter(Code_Option= option).exists():
                option_exists = False
        version_exists = Version.objects.filter(Code_Version = Code_Version).exists()

        return color_exists,option_exists,version_exists

        pass

    def __read_file(self, file_path, **kwargs):
        file_reader_factory = FileReaderFactory()
        file_reader = file_reader_factory.create_file_reader(**kwargs)
        file_content = file_reader.get_file_data(file_path)
        return file_content