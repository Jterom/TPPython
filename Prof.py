import Personne
import Eleve

class Prof:
    def __init__(self, nom):
        Personne.Personne.__init__(self,nom)
        self.Eleves = []

    def addEleve(self, Eleve):
        self.Eleves.insert(len(self.Eleves),Eleve)