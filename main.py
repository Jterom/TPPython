from tkinter import *
import Bus
import Eleve
import Prof

root = Tk()
root.title("Bus")
root.geometry("500x400")

listBus = []

# Fonction de création d'un Bus
def BusCrea():
    b = Bus.Bus(len(listBus))
    listBus.insert(len(listBus), 1)
    BBus = Button(root, text="Bus "+str(b.getNumBus()), command=lambda: View(b))
    Label(root, text="Bus "+str(b.getNumBus()))
    BBus.grid(row=1, column=int(b.getNumBus())+3)

#Page qui affiche les boutons pour ajouter des élèves ou des étudiants au bus sélectionné
def View(b):
    win = Toplevel(root)
    win.title("ajout eleve / prof")
    Verife = Button(win, text="vérifier que le bus peut partir", command=lambda: verification(win, b)).pack()

    Label(win, text="---------------").pack()

    nomProf = Entry(win)
    nomProf.pack()
    addProf = Button(win, text="ajouter le prof", command=lambda: ajoutProf(nomProf.get(), b)).pack()

    Label(win, text="---------------").pack()

    nomEleve = Entry(win)
    nomEleve.pack()
    nomEleve.insert(0, "Le nom de l'éleve")
    label = Label(win, text=nomEleve.get()).pack()
    classeEleve = Entry(win)
    classeEleve.pack()
    addEleve = Button(win, text="ajouter l'éléve",command=lambda: ajoutEleve(nomEleve.get(), classeEleve.get(), b)).pack()


#vérifie si le bus peut partir
def verification(win, b):
    if int(len(b.Eleves)+len(b.Prof)) > 0:
        label = Label(win, text=b.verifierPresent()).pack()




#permet d'ajouter un élève et de l'afficher en dessou du bus
def ajoutEleve(nom, classe, b):
    if int(len(b.Eleves)+len(b.Prof)) < int(b.Place) and int(len(b.Eleves)) < int(len(b.Prof))*10 and classe != "":
        if b.verifierClasse(classe) == 1:
            e = Eleve.Eleve(nom, classe)
            b.addEleve(e)
            b.attribEleve(e)
            btEleve = Button(root, text=nom, bg="white", command=lambda: elevePresent(e, root)).grid(row=int(len(b.Eleves))+int(len(b.Prof)+1), column=int(b.getNumBus())+3)


#la même chose que pour la fonction ajoutEleve mais pour les profs
def ajoutProf(nom, b):
    if int(len(b.Eleves)+len(b.Prof)) < int(b.Place):
        p = Prof.Prof(nom)
        b.addProf(p)
        if int(len(b.Prof)) ==1:
            buttonProf = Label(root, text=nom, bg="red").grid(row=int(len(b.Eleves)) + int(len(b.Prof) + 1), column=int(b.getNumBus())+3)
        else:
            buttonProf = Label(root, text=nom, bg="yellow").grid(row=int(len(b.Eleves)) + int(len(b.Prof) + 1), column=int(b.getNumBus())+3)




#passe un élève au statut présent
def elevePresent(e, root):
    e.present = 1

#fonction pour changer la couleur du bouton lorsqu'un élève est mis présent (ne marche pas)
#def change_color(root):
#    root.btEleve.configure(bg="green")

Button(root, text="Ajouter un Bus", command=BusCrea).grid(row=0, column=0)
Label(root, text="Pour mettre présent un élève cliquez dessus").grid(row=0, column=1)

root.mainloop()