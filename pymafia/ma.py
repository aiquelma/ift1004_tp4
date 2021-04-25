from tkinter import *
from framejoueur import FrameJoueurDroitBas, FrameJoueurDroitHaut, FrameJoueurGaucheBas, FrameJoueurGaucheHaut
from pymafia.partie import Partie


class DebuterJeu(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("900x600+500+300")
        self.main_container = Frame(self, width=900, height=300)
        #self.main_container.place(bordermode=OUTSIDE)
        self.main_container.grid(row=0, column=0, columnspan=100)
        self.top_frame = Frame(self.main_container, background="green")
        self.bottom_frame = Frame(self.main_container, background="yellow")
        self.top_frame.grid(row=0, column=0, columnspan=20, rowspan=20)
        self.bottom_frame.grid(row=20, column=0, columnspan=20, rowspan=20)
        self.premiere_fenetre()

    def premiere_fenetre(self):
        nbJoueur = StringVar()
        self.title("PyMafia - Débuter une partie")
        instruction1 = Label(self.top_frame)
        instruction1['text'] = "Veuillez choisir le nombre de joueurs: "
        instruction1.grid(row=0, column=0, columnspan=3)
        choixNbJoueurs = ["2", "3", "4"]
        nbJoueur = StringVar(None)
        nbJoueur.set(choixNbJoueurs[0])
        radiobuttons = list()
        self.totalJoueurs = OptionMenu(self.top_frame, nbJoueur, *choixNbJoueurs,
                                       command=lambda event: self.changementDropdown(self.framechoix,
                                                                                     radiobuttons, nbJoueur))
        self.totalJoueurs.grid(row=0, column=4)
        Label(self.top_frame, text="Veuillez choisir le type de joueur:",
                                                relief=FLAT, justify=LEFT)\
            .grid(row=1, column=0, columnspan=3)
        self.joueurVar, self.framechoix = self.créer_boutons_radios(self.top_frame, radiobuttons, int(nbJoueur.get()))

    def créer_boutons_radios(self, master, radiobuttons, nombre):
        # Création des boutons radios
        typeJoueur = [("Humain", 101, "Ordinateur", 102), ("Humain", 201, "Ordinateur", 202),
                      ("Humain", 301, "Ordinateur", 302), ("Humain", 401, "Ordinateur", 402)]
        radioButtonOffsetRow = 4
        radioButtonOffsetCol = 0
        joueurVar = list()
        joueurVarOffset = 0
        choixNbJoueurs = int
        if choixNbJoueurs == 2:
            radiobuttons.append += 1
        elif joueurVar == 3:
            radiobuttons.append += 2

        for joueurType1, joueurVal1, joueurType2, joueurVal2 in typeJoueur:
            if nombre > 0:
                joueurVar.append(StringVar())
                Label(master, text=f"Joueur {str(joueurVal1)[0]}").grid(row=radioButtonOffsetRow,
                                                                        column=radioButtonOffsetCol)
                Radiobutton(master, text=joueurType1, variable=joueurVar[joueurVarOffset],
                            value=joueurVal1, padx=0, pady=0, tristatevalue=1).\
                    grid(row=radioButtonOffsetRow, column=radioButtonOffsetCol)
                Radiobutton(master, text=joueurType2, variable=joueurVar[joueurVarOffset],
                            value=joueurVal2, padx=0, pady=0).\
                    grid(row=radioButtonOffsetRow, column=radioButtonOffsetCol + 1)
                joueurVar[joueurVarOffset].set(joueurVal1)  # Permet de sélectionner par défaut Humain
                radioButtonOffsetRow += 1
                joueurVarOffset += 1
            nombre -= 1
        return joueurVar, master

    def changementDropdown(self, master, radiobuttons, nbjoueurs):
        master.destroy()
        self.framechoix = Frame(self.top_frame)
        self.framechoix.grid(row=1, column=0, columnspan=3)
        self.framechoix['highlightthickness'] = 0
        self.framechoix['highlightbackground'] = 'black'
        self.labelChoixHumainOrdinateur = Label(self.top_frame, text="Veuillez choisir le type de joueur:",
                                                relief=FLAT,
                                                justify=LEFT,
                                                anchor="w")
        self.labelChoixHumainOrdinateur.grid(row=1, column=3, columnspan=3)
        self.joueurVar, self.framechoix = self.créer_boutons_radios(self.framechoix, radiobuttons, int(nbjoueurs.get()))


if __name__ == "__main__":
    jeu = DebuterJeu()
    jeu.mainloop()

