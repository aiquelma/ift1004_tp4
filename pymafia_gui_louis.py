from tkinter import Tk
from framejoueur import FrameJoueurDroitBas, FrameJoueurDroitHaut, FrameJoueurGaucheBas, FrameJoueurGaucheHaut
from pymafia.partie import Partie

class FenetrePymafia(Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMafia")
        self.resizable(0, 0)
        self.partie = Partie(4,0)
        self.partie.reinitialiser_dés_joueurs()

        self.framesJoueurs = [
            FrameJoueurGaucheHaut(self, self.partie.joueurs[0]),
            FrameJoueurDroitHaut(self, self.partie.joueurs[1]),
            FrameJoueurDroitBas(self, self.partie.joueurs[2]),
            FrameJoueurGaucheBas(self, self.partie.joueurs[3]),
        ]
        self.framesJoueurs[0].grid(row=1, column=0, padx=15, pady=15)
        self.framesJoueurs[1].grid(row=0, column=1, padx=15, pady=15)
        self.framesJoueurs[2].grid(row=1, column=2, padx=15, pady=15)
        self.framesJoueurs[3].grid(row=2, column=1, padx=15, pady=15)

if __name__ == '__main__':
    fenetre = FenetrePymafia()
    fenetre.mainloop()
