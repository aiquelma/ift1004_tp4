from tkinter import Tk, Menu, Button, IntVar, Label, OptionMenu, Toplevel
from framejoueur import FrameJoueurGauche, FrameJoueurDroit, FrameJoueurHaut, FrameJoueurBas

# partie = Partie
class NouvellePartie(Toplevel):
    def __init__(self):
        super().__init__()
        label = Label(self, text="Démarrer nouvelle partie")
        intvar = IntVar()
        optionMenu = OptionMenu(self, intvar, 3, 4, 5, 6)
        button = Button(self.)  # pas complet.
        button.grid(row=0, column=0)
class FenetrePymafia(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pymafia")
        self.resizable(0, 0)
        self.partie = (4, 0)
        self.partie.reinitialiser_dés_joueurs()

        self.framesjoueurs =[
            FrameJoueurGauche(self, self.partie.joueurs[0]),  # à compléter les emplacements de chacun.
            FrameJoueurDroit(self, self.partie.joueurs[1]),
            FrameJoueurHaut(self, self.partie.joueurs[2]),
            FrameJoueurBas(self, self.partie.joueurs[3])
        ]

        self.framejoueur[0].grid(row=1, colum=0, padx=15, pady=15)
        self.framejoueur[1].grid(row=0, colum=1, padx=15, pady=15)
        self.framejoueur[2].grid(row=1, colum=2, padx=15, pady=15)
        self.framejoueur[3].grid(row=2, colum=1, padx=15, pady=15)

        self.menu = Menu(self)
        self.premier_menu = Menu(self.menu, tearoff=0)
#        self.premier_menu.add_command(label='Nouvelle partie', command=lambda event: )  # pas complet.
        self.premier_menu.add_separator()
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)


    def fenetre_nouvelle_partie(self):
        fenetre - FenetrePymafia()
        print(fenetre.intvar.get())

if __name__ == '__main__':
    fenetre = FenetrePymafia()
    fenetre.mainloop()
