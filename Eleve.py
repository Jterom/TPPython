import Personne

class Eleve:
    def __init__(self, nom,  classe):
        Personne.Personne.__init__(self, nom)
        self.classe = classe
        self.present = 0

    # passe un eleve au statut présent
    def elevePresent(e):
        e.present = 1