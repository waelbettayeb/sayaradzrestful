from tarif.models import Tarif_Version, Tarif_Option, Tarif_Couleur
from dateutil.parser import parse


class Tarif_Builder():
    def Tarif_Handle(self,file):
        for row in file:
            r =  row.split(";")
            self.create_tarif(r)
        return True

    def create_tarif(self,r):
        if(r[0].strip()=="0"):
            self.save_version(r)
        elif(r[0].strip()=="0"):
            self.save_option(r)
        else:
            self.save_couleur(r)

    def save_version(r):
        cdv = r[1]
        dtd = parse(r[2])
        dtf = parse(r[3])
        px = float(r[4])
        tarif_Version = Tarif_Version.objects.create(Version = cdv, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
        tarif_Version.save()

    def save_option(r):
        cdo = r[1]
        dtd = parse(r[2])
        dtf = parse(r[3])
        px = float(r[4])
        tarif_Option = Tarif_Option.objects.create(Option = cdo, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
        tarif_Option.save()

    def save_couleur(r):
        cdc = r[1]
        dtd = parse(r[2])
        dtf = parse(r[3])
        px = float(r[4])
        tarif_Couleur = Tarif_Couleur.objects.create(Couleur = cdc, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
        tarif_Couleur.save()