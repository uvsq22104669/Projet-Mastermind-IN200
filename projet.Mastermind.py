# Groupe  LDDBI 5
# Laurédane COUSTILLAS
# Alexandre SCHOUMSKY
# Hippolyte LEFER
# Tilly SEASSAU
# https://github.com/uvsq22104669/Projet-Mastermind


# Import des librairies
import tkinter as tk
import random as rd

racine = tk.Tk()
racine.title("Mastermind")

# Définition des constantes
CANVAS_WIDTH, CANVAS_HEIGHT = 400, 600

canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.grid(column=0, row=1)

# Fonctions
def fermer_fenetre():
    """Fonction qui permet de fermer la fenêtre"""
    racine.destroy()

def mode_2joueurs ():
    """Fonction qui permet de jouer au Mastermind avec un mode de jeu de 2 joueurs"""
    pass

def mode_1joueur ():
    """Fonction qui permet de jouer au Mastermind avec un mode de jeu de 1 seul joueur"""
    pass
def cacher_code():
    """Fonction qui permet au joueur qui fait deviner le code de le cacher"""
    rectangle0 = canvas.create_rectangle(150,560,350,600, fill = "brown", outline="black")
    return



#création des widgets
bouton_quitter = tk.Button(racine, text="Quitter", bg ="white", command = fermer_fenetre)
bouton_2joueurs = tk.Button(racine, text= "2 Joueurs", bg= "grey", command = mode_2joueurs)
bouton_1joueur = tk.Button(racine, text= "1 Joueur", bg= "grey", command = mode_1joueur)
bouton_cacher = tk.Button(racine, text = "Cacher", bg = "white", command = cacher_code)

rectangle10 = canvas.create_rectangle(150,30,350,70, fill = "grey", outline="black")
rectangle9 = canvas.create_rectangle(150,80,350,120, fill = "grey", outline="black")
rectangle8 = canvas.create_rectangle(150,130,350,170, fill = "grey", outline="black")
rectangle7 = canvas.create_rectangle(150,180,350,220, fill = "grey", outline="black")
rectangle6 = canvas.create_rectangle(150,230,350,270, fill = "grey", outline="black")
rectangle5 = canvas.create_rectangle(150,280,350,320, fill = "grey", outline="black")
rectangle4 = canvas.create_rectangle(150,330,350,370, fill = "grey", outline="black")
rectangle3 = canvas.create_rectangle(150,380,350,420, fill = "grey", outline="black")
rectangle2 = canvas.create_rectangle(150,430,350,470, fill = "grey", outline="black")
rectangle1 = canvas.create_rectangle(150,480,350,520, fill = "grey", outline="black")
rectangle0 = canvas.create_rectangle(150,560,350,600, fill = "grey", outline="black")

cercle = canvas.create_oval(170,5,185,20, fill='blue', outline="black")
cercle = canvas.create_oval(190,5,205,20, fill='red', outline="black")
cercle = canvas.create_oval(210,5,225,20, fill='orange', outline="black")
cercle = canvas.create_oval(230,5,245,20, fill='yellow', outline="black")
cercle = canvas.create_oval(250,5,265,20, fill='green2', outline="black")
cercle = canvas.create_oval(270,5,285,20, fill='turquoise', outline="black")
cercle = canvas.create_oval(290,5,305,20, fill='violet', outline="black")
cercle = canvas.create_oval(310,5,325,20, fill='pink', outline="black")

cercle0 = canvas.create_oval(165,565,195,595, fill='white', outline="black")
cercle0 = canvas.create_oval(215,565,245,595, fill='white', outline="black")
cercle0 = canvas.create_oval(265,565,295,595, fill='white', outline="black")
cercle0 = canvas.create_oval(315,565,345,595, fill='white', outline="black")

cercle1 = canvas.create_oval(165,485,195,515, fill='white', outline="black")
cercle1 = canvas.create_oval(215,485,245,515, fill='white', outline="black")
cercle1 = canvas.create_oval(265,485,295,515, fill='white', outline="black")
cercle1 = canvas.create_oval(315,485,345,515, fill='white', outline="black")

cercle2 = canvas.create_oval(165,435,195,465, fill='white', outline="black")
cercle2 = canvas.create_oval(215,435,245,465, fill='white', outline="black")
cercle2 = canvas.create_oval(265,435,295,465, fill='white', outline="black")
cercle2 = canvas.create_oval(315,435,345,465, fill='white', outline="black")

cercle3 = canvas.create_oval(165,385,195,415, fill='white', outline="black")
cercle3 = canvas.create_oval(215,385,245,415, fill='white', outline="black")
cercle3 = canvas.create_oval(265,385,295,415, fill='white', outline="black")
cercle3 = canvas.create_oval(315,385,345,415, fill='white', outline="black")

cercle4 = canvas.create_oval(165,335,195,365, fill='white', outline="black")
cercle4 = canvas.create_oval(215,335,245,365, fill='white', outline="black")
cercle4 = canvas.create_oval(265,335,295,365, fill='white', outline="black")
cercle4 = canvas.create_oval(315,335,345,365, fill='white', outline="black")

cercle5 = canvas.create_oval(165,285,195,315, fill='white', outline="black")
cercle5 = canvas.create_oval(215,285,245,315, fill='white', outline="black")
cercle5 = canvas.create_oval(265,285,295,315, fill='white', outline="black")
cercle5 = canvas.create_oval(315,285,345,315, fill='white', outline="black")

cercle6 = canvas.create_oval(165,235,195,265, fill='white', outline="black")
cercle6 = canvas.create_oval(215,235,245,265, fill='white', outline="black")
cercle6 = canvas.create_oval(265,235,295,265, fill='white', outline="black")
cercle6 = canvas.create_oval(315,235,345,265, fill='white', outline="black")

cercle7 = canvas.create_oval(165,185,195,215, fill='white', outline="black")
cercle7 = canvas.create_oval(215,185,245,215, fill='white', outline="black")
cercle7 = canvas.create_oval(265,185,295,215, fill='white', outline="black")
cercle7 = canvas.create_oval(315,185,345,215, fill='white', outline="black")

cercle8 = canvas.create_oval(165,135,195,165, fill='white', outline="black")
cercle8 = canvas.create_oval(215,135,245,165, fill='white', outline="black")
cercle8 = canvas.create_oval(265,135,295,165, fill='white', outline="black")
cercle8 = canvas.create_oval(315,135,345,165, fill='white', outline="black")

cercle9 = canvas.create_oval(165,85,195,115, fill='white', outline="black")
cercle9 = canvas.create_oval(215,85,245,115, fill='white', outline="black")
cercle9 = canvas.create_oval(265,85,295,115, fill='white', outline="black")
cercle9 = canvas.create_oval(315,85,345,115, fill='white', outline="black")

cercle10 = canvas.create_oval(165,35,195,65, fill='white', outline="black")
cercle10 = canvas.create_oval(215,35,245,65, fill='white', outline="black")
cercle10 = canvas.create_oval(265,35,295,65, fill='white', outline="black")
cercle10 = canvas.create_oval(315,35,345,65, fill='white', outline="black")


# Position des widgets :
bouton_quitter.grid(column=1, row=5)
bouton_2joueurs.grid(column=1, row=0)
bouton_1joueur.grid(column=1, row=1)
bouton_cacher.grid (column = 0, row = 4, columnspan=3)


racine. mainloop()
