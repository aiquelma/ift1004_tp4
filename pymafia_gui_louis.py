from tkinter import Tk, RAISED, ACTIVE,DISABLED, Label, StringVar, OptionMenu
from framejoueur import FrameJoueurDroitBas, FrameJoueurDroitHaut, FrameJoueurGaucheBas, FrameJoueurGaucheHaut
from pymafia.partie import Partie


class FenetrePymafia(Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMafia")
        self.resizable(0, 0)
        self.partie = Partie(4, 0)
        self.partie.reinitialiser_dés_joueurs()
        self.framesJoueurs = [
            FrameJoueurGaucheHaut(self, self.partie.joueurs[0]),
            FrameJoueurDroitHaut(self, self.partie.joueurs[1]),
            FrameJoueurDroitBas(self, self.partie.joueurs[2]),
            FrameJoueurGaucheBas(self, self.partie.joueurs[3]),
        ]
        self.framesJoueurs[0].grid(row=0, column=0, padx=60, pady=60)
        self.framesJoueurs[1].grid(row=0, column=2, padx=60, pady=60)
        self.framesJoueurs[2].grid(row=2, column=2, padx=60, pady=60)
        self.framesJoueurs[3].grid(row=2, column=0, padx=60, pady=60)


class debutPartie(Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMafia - Débuter une partie")
        debuttxt = "Bienvenue à PyMafia, pour débuter une partie, veuillez indiquer le nombre de joueurs: "
        self.resizable(0, 0)
        self.label = Label(self, text=debuttxt, relief=RAISED)
        self.label.grid(row=0, column=0, padx=30, pady=30)
        choixNbJoueurs = ["1", "2", "3", "4"]
        nbJoueur = StringVar(self)
        nbJoueur.set(choixNbJoueurs[0])
        self.totalJoueurs = OptionMenu(self, nbJoueur, *choixNbJoueurs)
        self.totalJoueurs.grid(row=0, column=3,padx=30, pady=30)




if __name__ == '__main__':
    jouer = debutPartie()
    jouer.mainloop()

    # fenetre = FenetrePymafia()
    # fenetre.mainloop()
