from couleur.models import Couleur
from option.models import Option
from tarif.models import Tarif_Version, Tarif_Option, Tarif_Couleur
from dateutil.parser import parse

from version.models import Version


class Tarif_Builder():
    def Tarif_Handle(self,file):
        for raw in file:
            row = raw.decode("utf-8")
            r = row.split(";")
            self.create_tarif(r)
        return True

    def create_tarif(self,r):
        if(r[0].strip()=="0"):
            self.save_version(r)
        elif(r[0].strip()=="2"):
            self.save_option(r)
        else:
            self.save_couleur(r)

    def save_version(self,r):
        cdv = Version.objects.get(Code_Version = r[1])
        if cdv :
            dtd = parse(r[2])
            dtf = parse(r[3])
            px = float(r[4])
            tarif_Version = Tarif_Version.objects.create(Version = cdv, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
            tarif_Version.save()

    def save_option(self,r):
        cdo =  Option.objects.get(Code_Option = r[1])
        if cdo :
            dtd = parse(r[2])
            dtf = parse(r[3])
            px = float(r[4])
            tarif_Option = Tarif_Option.objects.create(Option = cdo, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
            tarif_Option.save()

    def save_couleur(self,r):
        cdc = Couleur.objects.get(Code_Couleur = r[1])
        if cdc :
            dtd = parse(r[2])
            dtf = parse(r[3])
            px = float(r[4])
            tarif_Couleur = Tarif_Couleur.objects.create(Couleur = cdc, Date_Debut = dtd, Date_Fin = dtf, Prix = px)
            tarif_Couleur.save()