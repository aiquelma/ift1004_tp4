from tkinter import Frame, Label, Button
from pymafia.joueur import Joueur


class FrameJoueur(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_joueur = Label(self, text=f"joueur{Joueur.identifiant}")
        self.label_des = Label(self, text=Joueur.des, font=("courrier", 32))
        self.button_des = Button(self, text="rouler les des")
        self.button_des.bind("<ButtonRelease-1>", lambda event: self.mettre_a_jour_des(Joueur))

    def metter_a_jour_des(self, joueur: Joueur):
        joueur.rouler_dés()
        self.label_des['text'] = joueur.dés

    def mettre_a_jour_des(self, joueur):
        pass


class FrameJoueurGauche(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")


class FrameJoueurDroit(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")


class FrameJoueurHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")


class FrameJoueurBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")
