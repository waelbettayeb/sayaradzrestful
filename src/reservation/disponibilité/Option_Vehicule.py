import json

from reservation.models import Vehicule, List_Option
from version.models import Version, Option_Version


class Options_de_vehicule():
    def get_list_options(self,nc):
        vehicule = Vehicule.objects.get(Numero_Chassis = nc)
        version = Version.objects.get(Code_Version = vehicule.Code_Version.Code_Version)
        option = List_Option.objects.filter(vehicule = nc)
        vopts = Option_Version.objects.filter(version = version.Code_Version).filter(Default = True)
        l = []
        l.extend(option)
        l.extend(vopts)
        l = [o.option.Code_Option for o in l]
        return l
    def get_options(self,nc):
        l = self.get_list_options(nc)
        options = str(l)
        return json.dumps(options)