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

rectangle10 = canvas.create_rectangle(150,60,350,100, fill = "white", outline="black")
rectangle9 = canvas.create_rectangle(150,110,350,150, fill = "white", outline="black")
rectangle8 = canvas.create_rectangle(150,160,350,200, fill = "white", outline="black")
rectangle7 = canvas.create_rectangle(150,210,350,250, fill = "white", outline="black")
rectangle6 = canvas.create_rectangle(150,260,350,300, fill = "white", outline="black")
rectangle5 = canvas.create_rectangle(150,310,350,350, fill = "white", outline="black")
rectangle4 = canvas.create_rectangle(150,360,350,400, fill = "white", outline="black")
rectangle3 = canvas.create_rectangle(150,410,350,450, fill = "white", outline="black")
rectangle2 = canvas.create_rectangle(150,460,350,500, fill = "white", outline="black")
rectangle1 = canvas.create_rectangle(150,510,350,550, fill = "white", outline="black")



# Position des widgets :
bouton_quitter.grid(column=1, row=3)
bouton_2joueurs.grid(column=1, row=0)
bouton_1joueur.grid(column=1, row=1)





racine. mainloop()
