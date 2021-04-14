from tkinter import *
from pymafia.joueur import Joueur

class fenetre_de_jeu(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.frame_left_top()
        self.frame_left_bottom()
        self.frame_right_top()
        self.frame_right_bottom()

    def frame_left_top(self):
        self.left_top = Frame(root, width=500, height=450, pady=5, bg="purple").grid(row=0, column=0)
        Label(self.left_top, text="Joueur 1").grid(row=0, column=0, sticky="wn")
        Text(self.left_top, height=1, width=55).grid(row=0, column=0, sticky="en")
        bouton = Button
        bouton(self.left_top, text="Roule les dés!", width=50, bg="white").grid(row=0, column=0, sticky="n")

    def frame_left_bottom(self):
        self.left_bottom = Frame(root, width=500, height=450, pady=5, bg="green").grid(row=1, column=0)
        Label(self.left_bottom, text="Joueur 3").grid(row=1, column=0, sticky="wn")
        Text(self.left_bottom, height=1, width=55).grid(row=1, column=0, sticky="en")

    def frame_right_top(self):
        self.right_top = Frame(root, width=500, height=450, pady=5, bg="darkblue").grid(row=0, column=1)
        Label(self.right_top, text="Joueur 2").grid(row=0, column=1, sticky="wn")
        Text(self.right_top, height=1, width=55).grid(row=0, column=1, sticky="en")

    def frame_right_bottom(self):
        self.right_bottom = Frame(root, width=500, height=450, pady=5, bg="black").grid(row=1, column=1)
        Label(self.right_bottom, text="Joueur 4").grid(row=1, column=1, sticky="wn")
        Text(self.right_bottom, height=1, width=55).grid(row=1, column=1, sticky="en")


class NouvellePartie(Toplevel):
    def __init__(self):
        super().__init__()
        label = Label(self, text="Démarrer nouvelle partie")
        label.grid(padx=2, pady=2)
        label.pack()
        intvar = IntVar()
        optionMenu = OptionMenu(self, intvar, 3, 4, 5, 6)
        boutonJ1 = Button(fenetre_de_jeu, text='rouler les dés')
        boutonJ1.grid(row=2, column=2, padx=3, pady=30)
        boutonJ1.pack

        self.menu = Menu(self)
        self.premier_menu = Menu(self.menu, tearoff=0)
        self.premier_menu.add_command(label='Jouer une nouvelle partie', command=NouvellePartie)
        self.premier_menu.add_command(label="Changer d'idée pis quitter finalement")
        self.premier_menu.add_separator()
        self.menu.add_cascade(label='Fichier', menu=self.premier_menu)
        self.config(menu=self.menu)


root = Tk()
root.title("Frames")
root.geometry("1000x1000")
app = fenetre_de_jeu(root)
N
root.mainloop()
