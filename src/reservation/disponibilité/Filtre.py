from reservation.serializers import Options_de_vehicule


class Filtre():

    def __init__(self,list):
        self.list = list

    def get_list(self):
        return self.list

    def filtrer_Marque(self, marque):
        if(marque):
            l = [v for v in self.list if (str(v.get_marque()) == str(marque))]
            self.list = l

    def filtrer_Modele(self,modele):
        if(modele):
            l = [v for v in self.list if (str(v.get_modele()) == str(modele))]
            self.list = l

    def filtrer_Version(self,version):
        if(version):
            l = [v for v in self.list if (str(v.Code_Version.Code_Version) == str(version))]
            self.list = l

    def filtrer_Couleur(self,couleur):
        if(couleur):
            l = [v for v in self.list if (str(v.Code_Couleur.Code_Couleur) == str(couleur))]
            self.list = l

    def filtrer_Option(self, options):
        if(options):
            p = Options_de_vehicule()
            l = [v for v in self.list if all((o in p.get_list_options(v.Numero_Chassis)) for o in options)]
            self.list = l