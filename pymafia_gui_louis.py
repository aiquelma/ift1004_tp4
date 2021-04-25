from tkinter import Tk, RAISED, ACTIVE, DISABLED, Label, StringVar, OptionMenu, Button, Menu, IntVar, Text, Toplevel, \
    Radiobutton, FLAT, LEFT, W, E, Frame
from framejoueur import FrameJoueurDroitBas, FrameJoueurDroitHaut, FrameJoueurGaucheBas, FrameJoueurGaucheHaut
from pymafia.partie import Partie
from random import randint


class FenetrePymafia(Tk):
    def __init__(self, nombre_de_joueurs):
        super().__init__()
        self.title("PyMafia")
        self.resizable(0, 0)
        self.partie = Partie(nombre_de_joueurs, nombre_de_joueurs)
        self.framesJoueurs = list()
        joueur_temporaire = FrameJoueurGaucheHaut(self, self.partie.joueurs[0])
        self.framesJoueurs.append(joueur_temporaire)
        self.framesJoueurs.append(FrameJoueurDroitHaut(self, self.partie.joueurs[1]))
        self.framesJoueurs[0].grid(row=0, column=0, padx=60, pady=60)
        self.framesJoueurs[1].grid(row=0, column=2, padx=60, pady=60)
        if nombre_de_joueurs >= 3:
            self.framesJoueurs.append(FrameJoueurDroitBas(self, self.partie.joueurs[2]))
            self.framesJoueurs[2].grid(row=2, column=2, padx=60, pady=60)
        if nombre_de_joueurs == 4:
            self.framesJoueurs.append(FrameJoueurGaucheBas(self, self.partie.joueurs[3]))
            self.framesJoueurs[3].grid(row=2, column=0, padx=60, pady=60)
        self.debuter_la_partie(self.partie)

    def debuter_la_partie(self, partie: Partie):
        hasard = randint(1, (len(self.framesJoueurs))) - 1
        partie.premier_joueur = self.framesJoueurs[hasard].joueur
        partie.joueur_courant = partie.premier_joueur
        partie.determiner_joueur_suivant()
        print(f"joueur {hasard + 1}")
        demande_de_sens = Label(self, text=f"Le premier joueur est le joueur {hasard + 1}, dans quel sens voulez-vous "
                                           f"jouer?", font=("courrier", 12), relief=FLAT)
        demande_de_sens.grid(row=0, column=0, padx=10, pady=10)
        bouton_select1 = Button(self, text="vers la gauche", font=("courrier", 12), pady=5, padx=5)
        bouton_select2 = Button(self, text="vers la droite", font=("courrier", 12), pady=5, padx=5)
        bouton_select1.bind("<ButtonRelease-1>", lambda event: self.sens_de_jeu(-1, bouton_select1, bouton_select2,
                                                                                demande_de_sens))
        bouton_select1.grid(row=1, column=0, sticky=W)
        bouton_select2.bind("<ButtonRelease-1>", lambda event: self.sens_de_jeu(1, bouton_select1, bouton_select2,
                                                                                demande_de_sens))
        bouton_select2.grid(row=1, column=0, sticky=E)
        for fj in self.framesJoueurs:
            fj.last_grid = fj.grid_info()
            fj.grid_forget()

    def sens_de_jeu(self, direction, bouton_select1, bouton_select2, demande_de_sens):
        self.partie.sens = direction
        bouton_select1.destroy()
        bouton_select2.destroy()
        demande_de_sens.destroy()
        for fj in self.framesJoueurs:
            fj.grid(column=fj.last_grid['column'], row=fj.last_grid['row'], padx=fj.last_grid['padx'],
                    pady=fj.last_grid['pady'])
        self.partie.reinitialiser_dés_joueurs()
        for fj in self.framesJoueurs:
            fj.joueur.mettre_a_jour_dés(fj.joueur)
        self.debuter_rondes()

    def debuter_rondes(self):
        self.identifier_joueur_courant()
        # for self.partie.joueurs in self.partie.joueurs_actifs:
        #     if self.partie.joueurs == self.partie.joueur_courant:
        #         self.partie.jouer_un_tour()
        pass

    def rouler_dé_complet(self):
        nombre_1, nombre_6 = self.partie.verifier_dés_joueur_courant_pour_1_et_6()
        self.label = Label(self.partie.afficher_messages_dés_1_et_6())

    def identifier_joueur_courant(self):
        for joueur in self.framesJoueurs:
            if self.partie.joueur_courant == joueur.joueur:
                joueur.rouler_dés_actif()
            else:
                joueur.rouler_dés_inactif()


class DebutPartie(Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMafia - Débuter une partie")
        self.resizable(0, 0)
        self.framesuperieur = Frame(self)
        self.framesuperieur.grid(row=0, column=0, columnspan=3)
        self.framesuperieur['highlightthickness'] = 0
        self.framesuperieur['highlightbackground'] = 'black'
        self.framechoix = Frame(self)
        self.framechoix.grid(row=1, column=0, columnspan=3)
        self.framechoix['highlightthickness'] = 0
        self.framechoix['highlightbackground'] = 'black'
        self.frameinferieur = Frame(self)
        self.frameinferieur.grid(row=4, column=0, columnspan=3)
        self.frameinferieur['highlightthickness'] = 0
        self.frameinferieur['highlightbackground'] = 'black'
        debuttxt = "Bienvenue à PyMafia, pour débuter une partie, veuillez indiquer le nombre de joueurs: "
        self.label = Label(self.framesuperieur , text=debuttxt, relief=FLAT)
        self.label.grid(row=0, column=0, padx=10, pady=10)
        # Création du DropDown
        choixNbJoueurs = ["2", "3", "4"]
        nbJoueur = StringVar(self)
        nbJoueur.set(choixNbJoueurs[0])
        radiobuttons = list()
        self.totalJoueurs = OptionMenu(self.framesuperieur, nbJoueur, *choixNbJoueurs,
                                       command=lambda event: self.changementDropdown(self.framechoix,
                                                                                     radiobuttons, nbJoueur))
        self.totalJoueurs.grid(row=0, column=1, padx=10, pady=10)
        # Fin DropDown
        self.labelChoixHumainOrdinateur = Label(self.framechoix, text="Veuillez choisir le type de joueur:",
                                                relief=FLAT,
                                                justify=LEFT,
                                                anchor="w")
        self.labelChoixHumainOrdinateur.grid(row=1, column=0, padx=10, pady=10)
        # Création bouton de démarrage de jeu ##
        self.debuterPartie = Button(self.frameinferieur,  text="Let's do this baby!")
        self.joueurVar, self.framechoix = self.créer_boutons_radios(self.framechoix, radiobuttons, int(nbJoueur.get()))

        # Juste le bouton ici:
        self.debuterPartie.bind("<ButtonRelease-1>", lambda event: self.commencerPartie(nbJoueur, self.joueurVar))
        self.debuterPartie.grid(row=int(nbJoueur.get()) + 2, column=1, padx=10, pady=10)
        self.creer_menu_fichier()

    def changementDropdown(self, master, radiobuttons, nbjoueurs):
        self.framechoix.destroy()
        self.framechoix = Frame(self)
        self.framechoix.grid(row=1, column=0, columnspan=3)
        self.framechoix['highlightthickness'] = 0
        self.framechoix['highlightbackground'] = 'black'
        self.labelChoixHumainOrdinateur = Label(self.framechoix, text="Veuillez choisir le type de joueur:",
                                                relief=FLAT,
                                                justify=LEFT,
                                                anchor="w")
        self.labelChoixHumainOrdinateur.grid(row=1, column=0, padx=10, pady=10)
        self.joueurVar, self.framechoix = self.créer_boutons_radios(self.framechoix, radiobuttons, int(nbjoueurs.get()))

        print("x")

        #self.joueurVar = self.créer_boutons_radios(radiobuttons, int(nbjoueurs.get()))

    def créer_boutons_radios(self, master, radiobuttons, nombre):
        # Création des boutons radios
        typeJoueur = [("Humain", 101, "Ordinateur", 102), ("Humain", 201, "Ordinateur", 202),
                      ("Humain", 301, "Ordinateur", 302), ("Humain", 401, "Ordinateur", 402)]
        radioButtonOffsetRow = 2
        radioButtonOffsetCol = 1
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
                                                                        column=radioButtonOffsetCol - 1)
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
        # Fin de création des boutons radios

    def commencerPartie(self, nbJoueur: StringVar, joueurVar):
        nombre_de_joueurs = int(nbJoueur.get())
        self.lireBoutonRadio(joueurVar)
        self.destroy()
        Jouer = FenetrePymafia(nombre_de_joueurs)
        Jouer.mainloop()

    def lireBoutonRadio(self, joueurVar):
        # À développer, il faut définir quel joueur dans la liste est un humain, quel ne l'est pas.
        # Ici, joueurVar contient la liste des choix des boutons radios
        # Cette fonction doit extraire le nombre de joueur humains, j'ai défini les joueurs humain par #XX1
        # ordinateurs par #XX2
        for jv in joueurVar:
            print(jv.get())
        pass

    def creer_menu_fichier(self):
        intvar = IntVar()
        self.menu = Menu(self)
        self.optionMenu = OptionMenu(self, intvar, 3, 4, 5, 6)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.premier_menu.add_command(label='Règlements', command=self.afficher_reglements)
        self.premier_menu.add_command(label='Recommencer partie')
        self.premier_menu.add_command(label='Pointage')
        self.premier_menu.add_separator()
        self.premier_menu.add_command(label='Quitter', command=self.destroy)
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)

    def afficher_reglements(self):
        reglements = Tk()
        reglements.title("Règlements")
        reglements.resizable(0, 0)
        regles = self.regles_jeu()
        label = Label(reglements, text=regles, relief=RAISED)
        label.grid(row=0, column=0, padx=10, pady=10)
        reglements.mainloop()

    def regles_jeu(self):
        return """Instructions\n\n,.-'¨'-.,-=-,.-'¨'-.,-= Pymafia =-,.-'¨'-.,-=-,.-'¨'-.,\n\n
          La partie peut se jouer avec un max de 8 joueurs mais nous suggérons fortement au moins 2.
          Les joueurs peuvent être humains ou ordinateurs ou les deux mais pas les trois.
          Les joueurs débutent avec chacun 50 points \"en banque\" et le but du jeux est de conserver le
          plus de points possible. Si un joueur n'a plus de points en banque, il quitte la partie.
          Le premier joueur à jouer est celui qui obtient le plus haut score en brassant chacun 2 dés.
          Le premier joueur doit déterminer si les tours seront croissant ou décroissant.
          \n\n,.-'¨'-.,-=-,.-'¨'-.,-= DéRoUlEmEnT dE lA pArTiE =-,.-'¨'-.,-=-,.-'¨'-.,\n
          Tous les joueurs reçoivent 5 dés et jouerons à tour de rôle selon le sens choisi.
          Lorsque le joueur_courant brasse un 1, il retire un dé de sa main. Lorsqu'il brasse un 6,
          il donne un dé au joueur suivant. Quand le joueur brasse un 2-3-4-5, il ne fais rien de particulier.
          Lorsque un joueur n'a plus de dés en main, la ronde est terminé, ce joueur a gagné la ronde.
          Les joueurs ayant encore des dés brassent leurs dés, soustraient ce pointage de leur banque et
          le donnent au joueur gagnant.
          La partie compte un maximum de 10 rondes et le gagnant est celui qui aura le plus haut score à
          la fin de ces 10 rondes à moins d'être le seul joueur à avoir des points avant ce temps."""


if __name__ == '__main__':
    jouer = DebutPartie()
    jouer.mainloop()

    # fenetre = FenetrePymafia()
    # fenetre.mainloop()
