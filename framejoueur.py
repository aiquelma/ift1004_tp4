from tkinter import Frame, Label, Button, DISABLED, ACTIVE
from pymafia.joueur import Joueur


class FrameJoueur(Frame):
    def __init__(self, master, joueur):
        """
        Classe qui gère le frame pour chaque joueurs.
        :param master: est le frame parent.
        :param joueur: définie la référence du joueur.
        """
        super().__init__(master)
        padding = " " * 110
        self.label_joueur = Label(self, text=f"Joueur {joueur.identifiant}\n{padding}")
        self.label_dés = Label(self, text=joueur.dés, font=("courrier", 32))
        self.button_dés = Button(self, text="rouler les dés", state=DISABLED,
                                 command=lambda: self.joueur_lance_dés(master, joueur))
        self.joueur = joueur
        self.last_grid = {}
        self['highlightthickness'] = 1
        self['highlightbackground'] = "black"

    def joueur_lance_dés(self, master, joueur: Joueur):
        """
        fonction qui met lance les dés des joueurs et met à jour l'affichage des dés. (événementiel relié au bouton).
        :param master: Classe parent.
        :param joueur: Définie la référence du joueur.
        :return: None
        """
        self.mettre_a_jour_dés(joueur)
        master.rouler_dé_complet()

    def mettre_a_jour_affichage_dés(self, joueur: Joueur):
        """
        Fonction qui met à jour l'affichage des dés.
        :param joueur: Définie la référence du joueur.
        :return: None
        """
        self.label_dés['text'] = joueur.dés

    def mettre_a_jour_dés(self, joueur: Joueur):
        """
        fonction qui met à jour les dés des joueurs. (événementiel relié au bouton).
        :param joueur: définie le référence du joueur.
        :return: None
        """
        joueur.rouler_dés()
        self.label_dés['text'] = joueur.dés
        self.désactiver_dés()

    def activer_dés(self):
        """
        fonction qui active les dés du joueur courant.
        :return: None
        """
        self.button_dés['state'] = ACTIVE

    def désactiver_dés(self):
        """
        fonction qui déactive les dés du joueur lorsque son tour est passé.
        :return: None
        """
        self.button_dés['state'] = DISABLED


class FrameJoueurGaucheHaut(FrameJoueur):
    def __init__(self, master, joueur):
        """
        Classe qui crée le frame pour un joueur en particulier.
        :param master: en référence à la fenêtre mère de tkinter.
        :param joueur: Définie la référence du joueur.
        """
        super().__init__(master, joueur)
        self.label_joueur.grid(row=0, column=1)
        self.label_dés.grid(row=2, column=1)
        self.button_dés.grid(row=1, column=1)


class FrameJoueurDroitHaut(FrameJoueur):
    def __init__(self, master, joueur):
        """
        Classe qui crée le frame pour un joueur en particulier.
        :param master: en référence à la fenêtre mère de tkinter.
        :param joueur: Définie la référence du joueur.
        """
        super().__init__(master, joueur)
        self.label_joueur.grid(row=0, column=1)
        self.label_dés.grid(row=2, column=1)
        self.button_dés.grid(row=1, column=1)


class FrameJoueurGaucheBas(FrameJoueur):
    def __init__(self, master, joueur):
        """
        Classe qui crée le frame pour un joueur en particulier.
        :param master: en référence à la fenêtre mère de tkinter.
        :param joueur: Définie la référence du joueur.
        """
        super().__init__(master, joueur)
        self.label_joueur.grid(row=3, column=1)
        self.label_dés.grid(row=1, column=1)
        self.button_dés.grid(row=2, column=1)


class FrameJoueurDroitBas(FrameJoueur):
    def __init__(self, master, joueur):
        """
        Classe qui crée le frame pour un joueur en particulier.
        :param master: en référence à la fenêtre mère de tkinter.
        :param joueur: Définie la référence du joueur.
        """
        super().__init__(master, joueur)
        self.label_joueur.grid(row=3, column=1)
        self.label_dés.grid(row=1, column=1)
        self.button_dés.grid(row=2, column=1)
