from tkinter import Tk, RAISED, Label, StringVar, OptionMenu, Button, Menu, IntVar, \
    Radiobutton, FLAT, LEFT, W, E, NE, Frame, messagebox
from framejoueur import FrameJoueurDroitBas, FrameJoueurDroitHaut, FrameJoueurGaucheBas, FrameJoueurGaucheHaut
from pymafia.partie import Partie
from random import randint
from time import sleep

# Variable globale pour le ronde maximum qu'on peut jouer
RONDEMAX = 10

class FenetrePymafia(Tk):
    def __init__(self, nombre_de_joueurs):
        super().__init__()
        self.geometry("800x500")
        self.title("PyMafia")
        self.rondes = 1
        self.resizable(0, 0)
        self.framesJoueurs = list()
        self.main_container = Frame(self)
        self.main_container.grid(row=0, rowspan=10, column=8, columnspan=300, sticky="nsew")
        self.partie = self.créerPartie(nombre_de_joueurs)
        self.frameEtat = Frame(self.main_container)
        self.frameEtat.grid(row=0, column=8, columnspan=300, sticky="nsew")
        self.debuter_la_partie()

    def créerPartie(self, nombre_de_joueurs):
        partie = Partie(nombre_de_joueurs, nombre_de_joueurs)
        self.framesJoueurs.append(FrameJoueurGaucheHaut(self, partie.joueurs[0]))
        self.framesJoueurs.append(FrameJoueurDroitHaut(self, partie.joueurs[1]))
        self.framesJoueurs[0].grid(row=0, column=0, padx=15, pady=5)
        self.framesJoueurs[1].grid(row=0, column=2, padx=15, pady=5)
        if nombre_de_joueurs >= 3:
            self.framesJoueurs.append(FrameJoueurDroitBas(self, partie.joueurs[2]))
            self.framesJoueurs[2].grid(row=2, column=2, padx=15, pady=5)
        if nombre_de_joueurs == 4:
            self.framesJoueurs.append(FrameJoueurGaucheBas(self, partie.joueurs[3]))
            self.framesJoueurs[3].grid(row=2, column=0, padx=15, pady=5)
        return partie

    def debuter_la_partie(self):
        self.déterminer_premier_joueur()
        self.demander_sens()

    def déterminer_premier_joueur(self):
        self.partie.premier_joueur = self.framesJoueurs[randint(1, (len(self.framesJoueurs))) - 1].joueur
        self.partie.joueur_courant = self.partie.premier_joueur

    def demander_sens(self):
        LabelText = f"Le Joueur {self.partie.premier_joueur.identifiant} jouera en premier. " \
                    f"Veuillez choisir dans quel sens nous devons jouer."
        demande_de_sens = Label(self, text=LabelText, font=("courrier", 12), relief=FLAT)
        demande_de_sens.grid(row=0, column=0, padx=10, pady=10)

        bouton_select1 = Button(self, text="Sens horaire", font=("courrier", 12), pady=5, padx=5)
        bouton_select2 = Button(self, text="Sens anti-horaire", font=("courrier", 12), pady=5, padx=5)
        bouton_select1.bind("<ButtonRelease-1>", lambda event: self.choix_sens(1, bouton_select1, bouton_select2,
                                                                               demande_de_sens))
        bouton_select1.grid(row=1, column=0, sticky=E)
        bouton_select2.bind("<ButtonRelease-1>", lambda event: self.choix_sens(-1, bouton_select1, bouton_select2,
                                                                               demande_de_sens))
        bouton_select2.grid(row=1, column=0, sticky=W)
        for fj in self.framesJoueurs:
            fj.last_grid = fj.grid_info()
            fj.grid_forget()
        self.frameEtat.grid_forget()

    def choix_sens(self, direction, bouton_select1, bouton_select2, demande_de_sens):
        bouton_select1.destroy()
        bouton_select2.destroy()
        demande_de_sens.destroy()
        self.partie.sens = direction
        self.partie.determiner_joueur_suivant()
        for fj in self.framesJoueurs:
            fj.grid(column=fj.last_grid['column'], row=fj.last_grid['row'], padx=fj.last_grid['padx'],
                    pady=fj.last_grid['pady'])
        self.partie.reinitialiser_dés_joueurs()
        for fj in self.framesJoueurs:
            fj.mettre_a_jour_affichage_dés(fj.joueur)
        self.créer_état(f"Joueur {self.partie.premier_joueur.identifiant} débutera la partie")

    def créer_état(self, MessageEtat=""):
        for child in self.frameEtat.winfo_children():
            child.destroy()
        self.frameEtat.grid(row=0, column=8, rowspan=300, sticky="nsew")
        self.statusFrameJoueurs = list()
        ligne = 0
        self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"Score\t\t", anchor=NE).grid(row=0, column=0))
        for fj in self.framesJoueurs:
            self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"Joueur {fj.joueur.identifiant}\t" \
                                                                      f"-->\t{fj.joueur.score}") \
                                           .grid(row=1 + ligne, column=0))
            ligne += 1
        self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"\nNombre de rondes\t{self.partie.ronde}\n\n")
                                       .grid(row=2 + ligne, column=0))
        message_generaux = list()
        self.statusFrameJoueurs.append(message_generaux)
        self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"Messages\t\t\n\n{MessageEtat}") \
                                       .grid(row=3 + ligne, column=0))
        self.debuter_rondes()

    def debuter_rondes(self):
        self.activer_dés_joueur_courant()
        self.maj_des()

    def rouler_dé_complet(self):
        nombre_1, nombre_6 = self.partie.verifier_dés_joueur_courant_pour_1_et_6()
        for joueur in self.framesJoueurs:
            joueur.mettre_a_jour_affichage_dés(joueur.joueur)
        message_dé1 = ""
        message_dé6 = ""
        if nombre_1 > 0:
            message_dé1 = f"Vous avez obtenu {nombre_1} dé 1"
        if nombre_6 > 0:
            message_dé1 = f"Vous avez obtenu {nombre_1} dé 6"
        self.afficher_déplacement_dés(nombre_1, nombre_6)
        self.partie.deplacer_les_dés_1_et_6(nombre_1, nombre_6)
        for joueur in self.framesJoueurs:
            joueur.mettre_a_jour_affichage_dés(joueur.joueur)
        if self.partie.verifier_si_fin_de_ronde():
            for joueur in self.framesJoueurs:
                joueur.désactiver_dés()
            message = f"Le joueur {self.partie.joueur_courant.identifiant} a gagné la ronde " \
                    f"{self.partie.ronde}. Cliquer OK pour calculer jouer les dés de fin de ronde et " \
                        f"calculer les points."
            messagebox.showinfo("Fin de ronde", message)
            self.partie.jouer_dés_en_fin_de_ronde()
            self.maj_des()
            message = self.partie.messages_pour_points_fin_de_ronde()
            messagebox.showinfo("Calcul de points", message)
            points_au_gagnant = self.partie.ajuster_points_des_perdants_en_fin_de_ronde()
            self.partie.ajuster_points_du_gagnant(points_au_gagnant)
            self.partie.passer_a_la_ronde_suivante()
            self.partie.retirer_joueurs_sans_points()
            if self.partie.ronde <= RONDEMAX and self.nombre_joueur_actifs() > 1:
                self.créer_état()
                self.partie.reinitialiser_dés_joueurs()
                self.maj_des()
            else:
                'fin du jeu'
        else:
            self.partie.passer_au_prochain_joueur()
            self.activer_dés_joueur_courant()
            self.maj_des()

    def nombre_joueur_actifs(self):
        """
        Cette fonction retourne le nombre de joueurs actifs d'une partie
        :return: int : Nombre de joueurs actifs
        """
        return len(self.partie.joueurs_actifs)

    def afficher_déplacement_dés(self, nombre_1, nombre_6):
        message_final = f"Le Joueur {self.partie.joueur_courant.identifiant} roule ses dés!\n"
        if nombre_1 + nombre_6 > 0:
            if nombre_1 > 0:
                pluriel = '' if nombre_1 == 1 else 's'
                message_1 = f"Il obtient {nombre_1} dé{pluriel} 1.\n" \
                            f"Ce{pluriel} dé{pluriel} {'seront' if pluriel == 's' else 'sera'} retiré{pluriel}.\n"
            if nombre_6 > 0:
                pluriel = '' if nombre_1 == 1 else 's'
                message_6 = f"Il obtient {nombre_6} dé{pluriel} 6.\n Ce{pluriel} dé{pluriel} sera donc transféré au " \
                            f"joueur suivant: Joueur {self.partie.joueur_suivant.identifiant}.\n"
            if nombre_1 > 0:
                message_final = message_final + message_1
            if nombre_6 > 0:
                message_final = message_final + message_6
            self.créer_état(message_final)

    def maj_des(self):
        for joueur in self.framesJoueurs:
            joueur.mettre_a_jour_affichage_dés(joueur.joueur)

    def activer_dés_joueur_courant(self):
        for joueur in self.framesJoueurs:
            if self.partie.joueur_courant == joueur.joueur:
                joueur.activer_dés()
            else:
                joueur.désactiver_dés()


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
        self.label = Label(self.framesuperieur, text=debuttxt, relief=FLAT)
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
        self.debuterPartie = Button(self.frameinferieur, text="Let's do this baby!")
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
                            value=joueurVal1, padx=0, pady=0, tristatevalue=1). \
                    grid(row=radioButtonOffsetRow, column=radioButtonOffsetCol)
                Radiobutton(master, text=joueurType2, variable=joueurVar[joueurVarOffset],
                            value=joueurVal2, padx=0, pady=0). \
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
        self.premier_menu.add_command(label='Relancer une partie')
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