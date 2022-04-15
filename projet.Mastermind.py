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

#création des widgets
bouton_quitter = tk.Button(racine, text="Quitter", bg ="white", command = fermer_fenetre)
bouton_2joueurs = tk.Button(racine, text= "2 Joueurs", bg= "grey", command = mode_2joueurs)
bouton_1joueur = tk.Button(racine, text= "1 Joueur", bg= "grey", command = mode_1joueur)


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
cercle = canvas.create_oval(250,5,265,20, fill='green', outline="black")
cercle = canvas.create_oval(270,5,285,20, fill='turquoise', outline="black")
cercle = canvas.create_oval(290,5,305,20, fill='violet', outline="black")
cercle = canvas.create_oval(310,5,325,20, fill='pink', outline="black")



# Position des widgets :
bouton_quitter.grid(column=1, row=3)
bouton_2joueurs.grid(column=1, row=0)
bouton_1joueur.grid(column=1, row=1)





racine. mainloop()
