from tkinter import *


class Framejoueur():
    pass


class pymafia(Tk, Frame):
    def __init__(self):
        self.tk = Tk.__init__(self)
        self.titlebg=("Bienvenu dans Pymafia")
        intvar = IntVar()
        self.optionMenu = OptionMenu(self, intvar, 3, 4, 5, 6)
        self.frameJoueur = []
        self.menu = Menu(self)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.premier_menu.add_command(label='Règlements', command=self.reglements)
        self.premier_menu.add_command(label='Recommencer partie')
        self.premier_menu.add_command(label='Pointage')
        self.premier_menu.add_separator()
        self.premier_menu.add_command(label='Quitter', command=self.destroy)
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)
        Frame.__init__(self, self.tk)
        self.grid()
        self.frame_left_top()
        self.frame_left_bottom()
        self.frame_right_top()
        self.frame_right_bottom()

    def afficher_reglements(self):
        return """Instructions,.-'¨'-.,-=-,.-'¨'-.,-= Pymafia =-,.-'¨'-.,-=-,.-'¨'-.,
          La partie peut se jouer avec un max de 8 joueurs mais nous suggérons fortement au moins 2.
          Les joueurs peuvent être humains ou ordinateurs ou les deux mais pas les trois.
          Les joueurs débutent avec chacun 50 points \"en banque\" et le but du jeux est de conserver le
          plus de points possible. Si un joueur n'a plus de points en banque, il quitte la partie.
          Le premier joueur à jouer est celui qui obtient le plus haut score en brassant chacun 2 dés.
          Le premier joueur doit déterminer si les tours seront croissant ou décroissant.
          \t\t\t,.-'¨'-.,-=-,.-'¨'-.,-= DéRoUlEmEnT dE lA pArTiE =-,.-'¨'-.,-=-,.-'¨'-.,
          Tous les joueurs reçoivent 5 dés et jouerons à tour de rôle selon le sens choisi.
          Lorsque le joueur_courant brasse un 1, il retire un dé de sa main. Lorsqu'il brasse un 6,
          il donne un dé au joueur suivant. Quand le joueur brasse un 2-3-4-5, il ne fais rien de particulier.
          Lorsque un joueur n'a plus de dés en main, la ronde est terminé, ce joueur a gagné la ronde.
          Les joueurs ayant encore des dés brassent leurs dés, soustraient ce pointage de leur banque et
          le donnent au joueur gagnant.
          La partie compte un maximum de 10 rondes et le gagnant est celui qui aura le plus haut score à
          la fin de ces 10 rondes à moins d'être le seul joueur à avoir des points avant ce temps."""


    def debuterPartie(self):
        self.label = Label(self, fg="000")
        self.label.grid(padx=200, pady=200)
        self.label["text"] = "écrit kekchose ici"

    def reglements(self):
        self.frame = Frame(self, width=550, height=500, bg="darkgrey").grid(row=0, column=0)
        self.label = Label(self.frame, text="afficher_reglements", bg='pink', fg='black')
        self.label.grid(row=0, column=0)
        self.label['text'] = self.afficher_reglements()
        self.label.bind("<Button-1>", lambda event: self.cacher_reglements(self.frame))


    def cacher_reglements(self, frame):
        frame.destroy()



Jeu = pymafia()
Jeu.mainloop()
