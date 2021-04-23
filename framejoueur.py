from tkinter import Frame, Label, Button, DISABLED, ACTIVE
from pymafia.joueur import Joueur
from pymafia.partie import Partie

class FrameJoueur(Frame):
    def __init__(self, master, joueur):
        super().__init__(master)
        self.label_joueur = Label(self, text=f"joueur{joueur.identifiant}")
        self.label_dés = Label(self, text=joueur.dés, font=("courrier", 32))
        self.button_dés = Button(self, text="rouler les dés", state=DISABLED)
        self.button_dés.bind("<ButtonRelease-1>", lambda event: self.mettre_a_jour_dés(joueur))
        ### essayer le self.button_dés.configure - voir la documentation
        # for joueur.identifiant in joueur:
        #     if joueur.identifiant == self.joueur_courant:
        #         self.button_dés = Button(self, text="rouler les dés", state=ACTIVE)
        #         self.button_dés.bind("<ButtonRelease-1>", lambda event: self.mettre_a_jour_dés(joueur))
        self.joueur = joueur
        self.last_grid = {}

    def mettre_a_jour_dés(self, joueur: Joueur):
        joueur.rouler_dés()
        self.label_dés['text'] = joueur.dés
        return


class FrameJoueurGaucheHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=0, column=1)
        self.label_dés.grid(row=2, column=1)
        self.button_dés.grid(row=1, column=1)


class FrameJoueurDroitHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=0, column=1)
        self.label_dés.grid(row=2, column=1)
        self.button_dés.grid(row=1, column=1)


class FrameJoueurGaucheBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=3, column=1)
        self.label_dés.grid(row=1, column=1)
        self.button_dés.grid(row=2, column=1)


class FrameJoueurDroitBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=3, column=1)
        self.label_dés.grid(row=1, column=1)
        self.button_dés.grid(row=2, column=1)
