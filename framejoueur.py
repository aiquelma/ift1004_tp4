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


class FrameJoueurGaucheHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")


class FrameJoueurDroitHaut(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")


class FrameJoueurGaucheBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)
        boutonJ1 = Button(text='rouler les dés')
        boutonJ1.grid(row=2, column=2)
        boutonJ1.pack

        button_des = Button(self, text="rouler les dés")


class FrameJoueurDroitBas(FrameJoueur):
    def __init__(self, master, joueur):
        super().__init__(master, joueur)
        self.label_des['wrapLength'] = 1
        self.label_joueur.grid(row=0, column=0)
        self.label_des.grid(row=0, column=1)
        self.label_des['wrapLength'] = 1
        self.button_des.grid(row=0, column=2)

        button_des = Button(self, text="rouler les dés")
