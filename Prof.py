import Personne
import Eleve

class Prof:
    def __init__(self, nom):
        Personne.Personne.__init__(self,nom)
        self.Eleves = []

#Fonction qui ajoute un élève à la liste Eleves d'un prof (limitée à 10)
    def addEleve(self, Eleve):
        self.Eleves.insert(len(self.Eleves),Eleve)