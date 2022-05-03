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
    #Creation du code secret 
    cerclecode_1 = random.randint(0,7)
    cerclecode_2 = random.randint(0,7)
    cerclecode_3 = random.randint(0,7)
    cerclecode_4 = random.randint(0,7)

    #association d'une couleur par nombre 
    if cerclecode_1 == 0 :
      cerclecode_1 = "blue"
    elif cerclecode_1 == 1 : 
      cerclecode_1 = "red"
    elif cerclecode_1 == 2 : 
      cerclecode_1 = "orange"
    elif cerclecode_1 == 3 : 
      cerclecode_1 = "yellow"
    elif cerclecode_1 == 4 : 
      cerclecode_1 = "green"
    elif cerclecode_1 == 5 : 
      cerclecode_1 = "turquoise"
    elif cerclecode_1 == 6 : 
      cerclecode_1 = "violet"
    elif cerclecode_1 == 7 :
      cerclecode_1 = "pink"

    if cerclecode_2 == 0 :
      cerclecode_2 = "blue"
    elif cerclecode_2 == 1 : 
      cerclecode_2 = "red"
    elif cerclecode_2 == 2 : 
      cerclecode_2 = "orange"
    elif cerclecode_2 == 3 : 
      cerclecode_2 = "yellow"
    elif cerclecode_2 == 4 : 
      cerclecode_2 = "green"
    elif cerclecode_2 == 5 : 
      cerclecode_2 = "turquoise"
    elif cerclecode_2 == 6 : 
      cerclecode_2 = "violet"
    elif cerclecode_2 == 7 :
      cerclecode_2 = "pink"

    if cerclecode_3 == 0 :
      cerclecode_3 = "blue"
    elif cerclecode_3 == 1 : 
      cerclecode_3 = "red"
    elif cerclecode_3 == 2 : 
      cerclecode_3 = "orange"
    elif cerclecode_3 == 3 : 
      cerclecode_3 = "yellow"
    elif cerclecode_3 == 4 : 
      cerclecode_3 = "green"
    elif cerclecode_3 == 5 : 
      cerclecode_3 = "turquoise"
    elif cerclecode_3 == 6 : 
      cerclecode_3 = "violet"
    elif cerclecode_3 == 7 :
      cerclecode_3 = "pink"

    if cerclecode_4 == 0 :
      cerclecode_4 = "blue"
    elif cerclecode_4 == 1 : 
      cerclecode_4 = "red"
    elif cerclecode_4 == 2 : 
      cerclecode_4 = "orange"
    elif cerclecode_4 == 3 : 
      cerclecode_4 = "yellow"
    elif cerclecode_4 == 4 : 
      cerclecode_4 = "green"
    elif cerclecode_4 == 5 : 
      cerclecode_4 = "turquoise"
    elif cerclecode_4 == 6 : 
      cerclecode_4 = "violet"
    elif cerclecode_4 == 7 :
      cerclecode_4 = "pink"

    #print(cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4) #j'avais mis ça pour verifier les valeurs pour jouer 

    #Ce qui manque dans cette fonction c'est le remplissage des cercles au fur et à mesure des essais mais aussi la présence de petits cercles à côté de la rangé des cercles qu'on devinne au fur et à mesure
    for i in range(10) :
      guess1 = input("What colour is circle 1?")
      guess2 = input("What colour is circle 2?") 
      guess3 = input("What colour is circle 3?")
      guess4 = input("What colour is circle 4?")
      #faudrait remplir les cercles de i-ième essai avec les couleurs choisies (en soit ça devrait se faire avec cercle-i (fill = guess1) ) très grossièrement

      question1 = input("Do you want to change one or more guesses? Please answer yes or no")
      if question1 == "yes" : 
          question1_1 = int(input("How many guesses would you like to change?"))
          for k in range(question1_1) : 
            question2 = input("What guess would you like to change? Please answer as 'guess x' ")
            if question2 == "guess 1" : 
                guess1 = input("What colour is circle 1?")
            elif question2 == "guess 2" : 
                guess2 = input("What colour is circle 2?")
            elif question2 == "guess 3" : 
                guess3 = input("what colour is circle 3?")
            elif question2 == "guess 4" : 
                guess4 = input("What colour is circle 4?")
       #Pareil ici, où faudrait modifier le fill des cercles avec les nouvelles valeurs de guess1, guess2, guess3 et guess4

      BonPlacement = 0
      BonneCouleur = 0
      if guess1 == cerclecode_1 : 
        BonPlacement += 1
      elif guess1 == cerclecode_2 :
        BonneCouleur +=1
      elif guess1 == cerclecode_3 : 
        BonneCouleur +=1 
      elif guess1 == cerclecode_4 : 
        BonneCouleur+=1

      if guess2 == cerclecode_2 : 
        BonPlacement += 1
      elif guess2 == cerclecode_1 :
        BonneCouleur +=1
      elif guess2 == cerclecode_3 : 
        BonneCouleur +=1 
      elif guess2 == cerclecode_4 : 
        BonneCouleur+=1

      if guess3 == cerclecode_3 : 
        BonPlacement += 1
      elif guess3 == cerclecode_1 :
        BonneCouleur +=1
      elif guess3 == cerclecode_2 : 
        BonneCouleur +=1 
      elif guess3 == cerclecode_4 : 
        BonneCouleur+=1

      if guess4 == cerclecode_4 : 
        BonPlacement += 1
      elif guess4 == cerclecode_1 :
        BonneCouleur +=1
      elif guess4 == cerclecode_2 : 
        BonneCouleur +=1 
      elif guess4 == cerclecode_3 : 
        BonneCouleur+=1

      if BonPlacement == 4 : 
        print("Congrats, you've won!")
        break
        
      elif i == 9 and BonPlacement != 4 : 
        print("Good try, but you've lost, the correcte combination was", cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4 )
        #Ici, faudrait faire apparaître les 4 couleurs du code secret
      else: 
        print("You have", BonPlacement, "guesses correct and", BonneCouleur,"good guesses of the colours used")
        #Faut mettre à droite (ou à gauche, là où il y a la place quoi) des petits cercles indicatifs des essais. 
        #Donc faire apparaître "BonPlacement nombre" de petit cercle vert et "BonneCouleur nombre" de petit cercle jaune et faire en sorte que ces cercles restent fixe lors de la partie
        

    
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
