import Eleve
import Prof

class Bus:
    def __init__(self, numBus):
        self.numBus = numBus
        self.Eleves = []
        self.Prof = []
        self.Place = 20
        self.Classe = []

#Fonction pour ajouter un élève
    def addEleve(self, Eleve):
        self.Eleves.insert(len(self.Eleves),Eleve)

#Fonction pour ajouter un prof
    def addProf(self, Prof):
        self.Prof.insert(len(self.Prof), Prof)

#Fonction pour savoir sur quel Bus de la liste on se trouve
    def getNumBus(self):
        return self.numBus

#appelle la méthode addEleve de Prof pour chaque élève et chaque prof
    def attribEleve(self, e):
        i=0
        for p in self.Prof:
            if i == 0:
                p.addEleve(e)
            i = i+1

#verifie si il y a plus de 3 classe dans un bus
    def verifierClasse(self, classe):
        for c in self.Classe:
            if c == classe:
                return 1
        if int(len(self.Classe)) <3:
            self.Classe.append(classe)
            return 1
        else:
            return 0

#vérifie si tout les eleves sont présents
    def verifierPresent(self):
        for e in self.Eleves:
            if e.present == 0:
                return "Le bus n'est pas prêt"

        return "Le bus est prêt"