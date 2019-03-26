import json

from reservation.disponibilité.Filtre import Filtre
from reservation.models import Vehicule


class Recherche_Hundler():

    def disponible(self, critere):
        c = json.loads(critere)
        v = Vehicule.objects.filter(Reservation = None)
        f = Filtre(v)
        try:
            f.filtrer_Marque(c["marque"])
            f.filtrer_Modele(c["modele"])
            f.filtrer_Version(c["version"])
            f.filtrer_Couleur(c["couleur"])
            f.filtrer_Option(c["option"])
            l = f.get_list()
            if(l):
                return [o.Numero_Chassis for o in l]
            else:
                return False
        except:
            return "erreur"