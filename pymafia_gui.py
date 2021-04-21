from tkinter import Tk, Frame, Button, OptionMenu, IntVar, Menu, Label, StringVar

class Framejoueur():
    pass


class Pymafia(Tk):
    def __init__(self):
        super().__init__()
        self.creer_menu_fichier()
        self.resizable(0, 0)
        self['height'] = 800
        self['width'] = 800
        self.title("BiEnVeNuE a MoN JeU dE pYmAfIa")
        self.debuterPartie()

    def creer_menu_fichier(self):
        intvar = IntVar()
        self.menu = Menu(self)
        self.optionMenu = OptionMenu(self, intvar, 3, 4, 5, 6)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.premier_menu.add_command(label='Règlements', command=self.rien)
        self.premier_menu.add_command(label='Recommencer partie')
        self.premier_menu.add_command(label='Pointage')
        self.premier_menu.add_separator()
        self.premier_menu.add_command(label='Quitter', command=self.destroy)
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)

    def rien(self):
        pass

    def debuterPartie(self):
        frame = Frame(self, width=400, height=400).grid(row=4, column=3)
        label = self.creerLabel(frame, fgcolor="black", bgcolor="pink", rowpos=0, columnpos=0, anchorpos="nw", rs=3)
        label["text"] = "Débuter une partie"
        label_partie = self.creerLabel(frame, fgcolor="black", bgcolor="purple", rowpos=4, columnpos=0, anchorpos="w")
        label_partie['text'] = "Veuillez sélectionner le nombre de joueurs:"
        ddListe = ["1", "2", "3", "4"]
        frame2 = Frame(self, width=400, height=400)
        dd = self.creerDropDown(frame2, ddListe)
        dd.pack()

    def creerLabel(self, frame, fgcolor, bgcolor, rowpos, columnpos, anchorpos, cs=1, rs=1):
        self.label = Label(frame, fg=fgcolor, bg=bgcolor)
        self.label.grid(column=columnpos, row=rowpos)
        self.label.anchor(anchorpos)
        return self.label

    def creerDropDown(self, frame, elements):
        valeurs = StringVar(self)
        valeurs.set("1")
        dd = OptionMenu(self, valeurs, elements)
        return dd

Jeu = Pymafia()

Jeu.mainloop()