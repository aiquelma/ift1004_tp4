from tkinter import Tk, RAISED, Label, StringVar, OptionMenu, Button, Menu, IntVar, \
    Radiobutton, FLAT, LEFT, W, E, Frame, messagebox
from framejoueur import FrameJoueurDroitBas, FrameJoueurDroitHaut, FrameJoueurGaucheBas, FrameJoueurGaucheHaut
from pymafia.partie import Partie
from random import randint

# Variable globale pour le ronde maximum qu'on peut jouer
RONDEMAX = 2


class FenetrePymafia(Tk):
    def __init__(self, nombre_de_joueurs):
        """
        Initialisation de pyMafia GUI
        :param nombre_de_joueurs: Nombre de joueurs humains
        """
        super().__init__()
        self.geometry("900x800")
        self.title("PyMafia")
        self.rondes = 1
        self.resizable(0, 0)
        self.framesJoueurs = list()
        self.main_container = Frame(self)
        self.main_container.grid(row=3, rowspan=10, column=0, columnspan=300, sticky="nsew")
        self.partie = self.créer_partie(nombre_de_joueurs)
        self.frameEtat = Frame(self.main_container)
        self.frameEtat.grid(row=0, column=8, columnspan=300, sticky="nsew")
        self.debuter_la_partie()
        self.partie_en_cours = True
        self.statusFrameJoueurs = list()
        self.intvar = IntVar()
        self.menu = Menu(self)
        self.optionMenu = OptionMenu(self, self.intvar, 3, 4, 5, 6)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.menu = Menu(self)
        self.optionMenu = OptionMenu(self, self.intvar, 3, 4, 5, 6)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.premier_menu.add_command(label='Relancer une partie', command=self.nouvelle_partie)
        self.premier_menu.add_separator()
        self.premier_menu.add_command(label='Quitter', command=self.destroy)
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)

    def créer_partie(self, nombre_de_joueurs):
        """
        Crée les sous-frames contenant les joueurs
        :param nombre_de_joueurs:
        :return: référence vers la partie créée
        """
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
        """
        Demande au joueur qui débute dans quel sens il désire débuter
        normalement j'aurais gossé pour que si y'ait deux joueurs ça ne demande pas le sens
        mais ça ne me tente pas
        :return:
        """
        label_txt = f"Le Joueur {self.partie.premier_joueur.identifiant} jouera en premier. " \
                    f"Veuillez choisir dans quel sens nous devons jouer."
        demande_de_sens = Label(self, text=label_txt, font=("courrier", 12), relief=FLAT)
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
        """
        Effectue le choix du sens (anti) horaire pour le jeu. Événementiel aux boutons de choix de sens
        :param direction: 1 - horaire, -1 antihoraire
        :param bouton_select1: référence au bouton à détruire
        :param bouton_select2: référence au bouton à détruire
        :param demande_de_sens: référence au label à détruire
        :return: None
        """
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

    def créer_état(self, message_etat=" " * 40):
        """
        Créer frame en bas de fenêtre pour afficher le score et les messages du jeu
        :param message_etat: Message optionnel qui doit être afficher dans la fenêtre de jeu
        :return:
        """
        for child in self.frameEtat.winfo_children():
            child.destroy()
        self.frameEtat.grid(row=3, column=0, rowspan=300, sticky="nsew")
        self.statusFrameJoueurs = list()
        ligne = 0
        self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"Score", justify=LEFT).grid(row=0, column=0))
        for fj in self.framesJoueurs:
            self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"Joueur {fj.joueur.identifiant}"
                                                                      f"-->\t{fj.joueur.score}",  justify=LEFT)
                                           .grid(row=2 + ligne, column=0))
            ligne += 1
        self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"Nombre de rondes\t{self.partie.ronde}\n\n",
                                             justify=LEFT).grid(row=3 + ligne, column=0))
        self.statusFrameJoueurs.append(Label(self.frameEtat, text=f"\n\nMessages\t\t\n\n{message_etat}", justify=LEFT)
                                       .grid(row=4 + ligne, column=0))
        self.debuter_rondes()

    def debuter_rondes(self):
        """
        débute une ronde et mets à jour l'affichage de dés
        :return: None
        """
        if self.partie_en_cours:
            self.activer_dés_joueur_courant()
            self.maj_des()

    def gérer_dés_1_et_6(self):
        """
        Effectue la gestion des dés 1 à 6
        :return: None
        """
        nombre_1, nombre_6 = self.partie.verifier_dés_joueur_courant_pour_1_et_6()
        for joueur in self.framesJoueurs:
            joueur.mettre_a_jour_affichage_dés(joueur.joueur)
        if nombre_1 > 0:
            f"Vous avez obtenu {nombre_1} dé 1"
        if nombre_6 > 0:
            f"Vous avez obtenu {nombre_1} dé 6"
        self.afficher_déplacement_dés(nombre_1, nombre_6)
        self.partie.deplacer_les_dés_1_et_6(nombre_1, nombre_6)

    def gérer_fin_de_ronde(self):
        """
            Gère la fin de la ronde, joue les dés et attribut les points au gagnant
        :return: None
        """
        self.partie.jouer_dés_en_fin_de_ronde()
        self.maj_des()
        message = self.partie.messages_pour_points_fin_de_ronde()
        messagebox.showinfo("Calcul de points", message)
        points_au_gagnant = self.partie.ajuster_points_des_perdants_en_fin_de_ronde()
        self.partie.ajuster_points_du_gagnant(points_au_gagnant)
        self.partie.passer_a_la_ronde_suivante()
        self.partie.retirer_joueurs_sans_points()

    def passer_prochaine_ronde(self):
        """
        Vérifie si nous pouvons passer à la prochaine ronde
        :return: booléen
        """
        return self.partie.ronde <= RONDEMAX and self.nombre_joueur_actifs() > 1

    def créer_message_fin_de_partie(self):
        """
        Retourne chaine de caractère indiquant qui est le joueur gagnant
        :return: message définissant le joueur gagnant
        """
        indices_gagnant = self.partie.determiner_liste_gagnants()
        if len(indices_gagnant) == 1:
            gagnant = self.partie.joueurs[indices_gagnant[0]]
            message = f"Le gagnant est le Joueur {gagnant.identifiant}."
        else:
            message = f"Les joueurs gagnants sont les joueurs  "
            for indice in indices_gagnant:
                gagnant = self.partie.joueurs[indice]
                message = message + f"Joueur {gagnant.identifiant} "
        return message

    def gérer_fin_partie_ou_ronde(self):
        """
        Valide si c'est une fin de partie.
        :return:
        """
        if self.passer_prochaine_ronde():
            self.créer_état()
            self.partie.reinitialiser_dés_joueurs()
            self.maj_des()
        else:
            self.partie_en_cours = False
            self.désactiver_tous_les_dés()
            message = str(self.créer_message_fin_de_partie())
            self.créer_état(message)
            message = self.partie.message_points_en_fin_de_partie()
            message = message + "\nPour démarrer une nouvelle partie, utiliser le menu."
            messagebox.showinfo("Fin de la partie", message)

    def rouler_dé_complet(self):
        """
        Routine du jeu au complet
        Permet de voir si le jeu est encore en cours, ronde terminée, fin de la partie.

        :return:
        """
        self.gérer_dés_1_et_6()
        for joueur in self.framesJoueurs:
            joueur.mettre_a_jour_affichage_dés(joueur.joueur)
        if self.partie.verifier_si_fin_de_ronde():
            for joueur in self.framesJoueurs:
                joueur.désactiver_dés()
            message = f"Le joueur {self.partie.joueur_courant.identifiant} a gagné la ronde " \
                      f"{self.partie.ronde}. Cliquer OK pour calculer jouer les dés de fin de ronde et " \
                      f"calculer les points."
            messagebox.showinfo("Fin de ronde", message)
            self.gérer_fin_de_ronde()
            self.gérer_fin_partie_ou_ronde()
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
        """
            Ouvre un message box pour informer le joueur que des dés 1 et 6 ont étés pigés.

        :nombre_1 (int): nombre de dés 1
        :nombre_6 (int): nombre de dés 6
        :return: None
        """
        message_final = f"Le Joueur {self.partie.joueur_courant.identifiant} roule ses dés!\n"
        message_1 = ""
        message_6 = ""
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
        """
        Mets à jour le label contenant les valeurs des dés
        :return: None
        """
        for joueur in self.framesJoueurs:
            joueur.mettre_a_jour_affichage_dés(joueur.joueur)

    def désactiver_tous_les_dés(self):
        """
        Désactive le bouton Lancer dés pour tous les joueurs sur le frame
        :return: None
        """
        for joueur in self.framesJoueurs:
            joueur.désactiver_dés()

    def activer_dés_joueur_courant(self):
        """
        Cette fonction parcours les frames contenant des joueurs et active le bouton Lancer dés
        que si la partie est encore en cours.
        :return:
        """
        if self.partie_en_cours:
            for joueur in self.framesJoueurs:
                if self.partie.joueur_courant == joueur.joueur:
                    joueur.activer_dés()
                else:
                    joueur.désactiver_dés()
        else:
            self.désactiver_tous_les_dés()

    def nouvelle_partie(self):
        """
        Menu du logiciel - Relancer une partie - Permet de relancer une partie
        :return: None
        """
        if self.partie_en_cours:
            message = "Vous avez une partie en cours. Désirez-vous réellement lancer une nouvelle partie?"
            if messagebox.askokcancel("Annuler", message, default="cancel", icon="warning"):
                self.partie_en_cours = False
                self.destroy()
                DebutPartie()
        else:
            self.destroy()
            DebutPartie()


class DebutPartie(Tk):
    def __init__(self):
        """
        Cette fenêtre contient la configuration requise pour débuter le jeu PyMafia
        L'usager doit remplir les données requises avant de pouvoir débuter le jeu
        """
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
        self.frameinferieur.grid(row=2, column=0, columnspan=3)
        self.frameinferieur['highlightthickness'] = 0
        self.frameinferieur['highlightbackground'] = 'black'
        debuttxt = "Bienvenue à PyMafia, pour débuter une partie, veuillez indiquer le nombre de joueurs: "
        self.label = Label(self.framesuperieur, text=debuttxt, relief=FLAT)
        self.label.grid(row=0, column=0, padx=10, pady=10)
        # Création du DropDown
        choix_nb_joueurs = ["2", "3", "4"]
        nb_joueur = StringVar(self)
        nb_joueur.set(choix_nb_joueurs[0])
        radiobuttons = list()
        self.totalJoueurs = OptionMenu(self.framesuperieur, nb_joueur, *choix_nb_joueurs,
                                       command=lambda event: self.changement_dropdown(
                                                                                     radiobuttons, nb_joueur))
        self.totalJoueurs.grid(row=0, column=1, padx=10, pady=10)
        # Fin DropDown
        self.labelChoixHumainOrdinateur = Label(self.framechoix, text="Veuillez choisir le type de joueur:",
                                                relief=FLAT,
                                                justify=LEFT,
                                                anchor="w")
        self.labelChoixHumainOrdinateur.grid(row=1, column=0, padx=10, pady=10)
        self.debuterPartie = Button(self.frameinferieur, text="Let's do this baby!")
        self.joueurVar = self.créer_boutons_radios(radiobuttons, int(nb_joueur.get()))
        self.debuterPartie.bind("<ButtonRelease-1>", lambda event: self.commencer_partie(nb_joueur, self.joueurVar))
        self.debuterPartie.grid(row=int(nb_joueur.get()) + 2, column=1, padx=10, pady=10)
        intvar = IntVar()
        self.menu = Menu(self)
        self.optionMenu = OptionMenu(self, intvar, 3, 4, 5, 6)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.premier_menu.add_command(label='Règlements', command=self.afficher_reglements)
        self.premier_menu.add_separator()
        self.premier_menu.add_command(label='Quitter', command=self.destroy)
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)

    def changement_dropdown(self, radiobuttons, nbjoueurs):
        """
        fonction évenementielle qui détecte un changement dans le dropdown du nombre de joueur
        Elle recrée les boutons radios sur demande
        :radiobuttons (list): lien des boutons radios
        :nbjoueurs (int): valeur sélectionnée dans le dropdown
        :return:
        """
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
        self.joueurVar = self.créer_boutons_radios(radiobuttons, int(nbjoueurs.get()))

    def créer_boutons_radios(self, radiobuttons, nombre):
        """
        Cette fonction permet de créer/recréer les boutons radios selon le nombre de paramètres requis
        :param radiobuttons: La liste contenant les boutons radios créés
        :param nombre: Le nombre de boutons radios à créer (nombre de joueurs)
        :return: Retourne la variable des boutons radios ainsi que le frame
        """
        type_joueur = [("Humain", 101, "Ordinateur", 102), ("Humain", 201, "Ordinateur", 202),
                       ("Humain", 301, "Ordinateur", 302), ("Humain", 401, "Ordinateur", 402)]
        radio_button_offset_row = 2
        radio_button_offset_col = 1
        joueur_var = list()
        joueur_var_offset = 0
        choix_nb_joueurs = int
        if choix_nb_joueurs == 2:
            radiobuttons.append += 1
        elif joueur_var == 3:
            radiobuttons.append += 2

        for joueurType1, joueurVal1, joueurType2, joueurVal2 in type_joueur:
            if nombre > 0:
                joueur_var.append(StringVar())
                Label(self.framechoix, text=f"Joueur {str(joueurVal1)[0]}").grid(row=radio_button_offset_row,
                                                                                 column=radio_button_offset_col - 1)
                Radiobutton(self.framechoix, text=joueurType1, variable=joueur_var[joueur_var_offset],
                            value=joueurVal1, padx=0, pady=0, tristatevalue=1). \
                    grid(row=radio_button_offset_row, column=radio_button_offset_col)
                Radiobutton(self.framechoix, text=joueurType2, variable=joueur_var[joueur_var_offset],
                            value=joueurVal2, padx=0, pady=0). \
                    grid(row=radio_button_offset_row, column=radio_button_offset_col + 1)
                joueur_var[joueur_var_offset].set(joueurVal1)  # Permet de sélectionner par défaut Humain
                radio_button_offset_row += 1
                joueur_var_offset += 1
            nombre -= 1
        return joueur_var
        # Fin de création des boutons radios

    def commencer_partie(self, nb_joueur: StringVar, joueur_var):
        """
        Cette fonction permet de lancer le GUI du jeu PyMafia

        :param nb_joueur: La variable contenant le menu dropdown du nombre de joueurs
        :param joueur_var: Les valeurs des boutons radios indiquant humain ou ordinateur
        :return: None
        """
        nombre_de_joueurs = int(nb_joueur.get())
        self.lire_bouton_radio(joueur_var)
        self.destroy()
        jouer_partie = FenetrePymafia(nombre_de_joueurs)
        jouer_partie.mainloop()

    @staticmethod
    def lire_bouton_radio(joueur_var):
        # À développer, il faut définir quel joueur dans la liste est un humain, quel ne l'est pas.
        # Ici, joueur_var contient la liste des choix des boutons radios
        # Cette fonction doit extraire le nombre de joueur humains, j'ai défini les joueurs humain par #XX1
        # ordinateurs par #XX2
        # concept mauvais, on ne l'utilisera pas finalement, à développer pour le TP6 !
        #for jv in joueur_var:
        #    print(jv.get())
        pass

    def afficher_reglements(self):
        """
        Cette fonction affiche une fenêtre avec les règlements
        :return:
        """
        reglements = Tk()
        reglements.title("Règlements")
        reglements.resizable(0, 0)
        regles = self.regles_jeu()
        label = Label(reglements, text=regles, relief=RAISED)
        label.grid(row=0, column=0, padx=10, pady=10)
        Button(reglements, text="Fermer", command=reglements.destroy).grid(row=1, column=1)
        reglements.mainloop()

    @staticmethod
    def regles_jeu():
        """
        Fait que retourner un string avec les instructions du jeu
        :return: string : règles du jeu
        """
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
