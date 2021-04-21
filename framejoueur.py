from tkinter import Frame, Label, Button
from pymafia.joueur import Joueur
from pymafia.de import Dé
from pymafia.partie import Partie


class FrameJoueur(Frame):
    def __init__(self, master, joueur):
        super().__init__(master)
        self.label_joueur = Label(self, text=f"joueur{joueur.identifiant}")
        self.label_dés = Label(self, text=joueur.dés, font=("courrier", 32))
        self.button_dés = Button(self, text="rouler les dés")
        self.button_dés.bind("<ButtonRelease-1>", lambda event: self.mettre_a_jour_dés(joueur))

    def mettre_a_jour_dés(self, joueur: Joueur):
        Joueur.rouler_dés(self)
        self.label_dés['text'] = joueur.dés
        return


class FrameJoueurGaucheHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=0, column=1)
        self.label_dés.grid(row=2, column=1)
        self.button_dés.grid(row=1, column=1)
#        self.dés = Joueur.rouler_dés(self.dés)

#        self.button_dés = Button(self, text="rouler les dés")


class FrameJoueurDroitHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=0, column=1)
        self.label_dés.grid(row=2, column=1)
        self.button_dés.grid(row=1, column=1)
#        self.dés = Joueur.rouler_dés(self.dés)


class FrameJoueurGaucheBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=3, column=1)
        self.label_dés.grid(row=1, column=1)
        self.button_dés.grid(row=2, column=1)
#        self.dés = Joueur.rouler_dés(self.dés)

        button_des = Button(self, text="rouler les dés")


class FrameJoueurDroitBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_joueur.grid(row=3, column=1)
        self.label_dés.grid(row=1, column=1)
        self.button_dés.grid(row=2, column=1)
#        self.dés = Joueur.rouler_dés(self.dés)

        button_des = Button(self, text="rouler les dés")
