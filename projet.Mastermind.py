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
  #Valeurs utilisés plus tard pour le remplissage des  cercles grands et petis
  y0= -15
  y1= 15
  y0_petit=-4
  y1_petit= 6
  #Creation du code secret par un des joueurs 
  #Cercle code 1
  circle1 = input("What is the colour of circle 1?")
  canvas.create_oval(165,565,195,595, fill= circle1, outline="black")
  #Cercle code 2
  circle2 = input("What is the colour of circle 2?")
  canvas.create_oval(215,565,245,595, fill=circle2, outline="black")
  #cercle code 3
  circle3 = input("What is the colour of circle 3?")
  canvas.create_oval(265,565,295,595, fill=circle3, outline="black")
  #Cercle code 4
  circle4 = input("What is the colour of circle 4?")
  canvas.create_oval(315,565,345,595, fill=circle4, outline="black")

  question1 = input("Are you satisfied with your choices? Please answer yes or no")
  if question1 == "no" : 
    question2 = int(input("How many circles do you want to change?"))
    for k in range(question2) :
      question3 = ("What circle do you want to change? Please answer in the format 'circle x'")
      if question3 == "circle 1" : 
        circle1 = input("What colour is circle 1?")
        canvas.create_oval(165,565,195,595, fill= circle1, outline="black")
      elif question3 == "circle 2" : 
        circle2 = input("What colour is circle 2?")
        canvas.create_oval(215,565,245,595, fill=circle2, outline="black")
      elif question3 == "circle 3" : 
        circle3 = input("what colour is circle 3?")
        canvas.create_oval(265,565,295,595, fill=circle3, outline="black")
      elif question3 == "circle 4" : 
        circle4 = input("What colour is circle 4?")
        canvas.create_oval(315,565,345,595, fill=circle4, outline="black")
  
  print("Cliquez sur 'Cacher' pour cacher votre code et permettre à votre adversaire de jouer")
  
  for i in range(10) :
    #Valeurs utilisées pour la creation de cercle
    y0 += 50
    y1 += 50
    x0=115
    x1=145
    
    guess1 = input("What colour is circle 1?")
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess1, outline="black")
    guess2 = input("What colour is circle 2?")
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess2, outline="black")
    guess3 = input("What colour is circle 3?")
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess3, outline="black")
    guess4 = input("What colour is circle 4?")
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess4, outline="black")
    
    
    question1 = input("Do you want to change one or more guesses? Please answer yes or no")
    while question1 == "yes" : 
      question1_1 = int(input("How many guesses would you like to change?"))
      for k in range(question1_1) : 
        question2 = input("What guess would you like to change? Please answer as 'guess x' ")
        if question2 == "guess 1" : 
          guess1 = input("What colour is circle 1?")
        elif question2 == "guess 2" : 
          guess2 = input("What colour is circle 2?")
          x0
        elif question2 == "guess 3" : 
          guess3 = input("what colour is circle 3?")
        elif question2 == "guess 4" : 
          guess4 = input("What colour is circle 4?")
      question3 = input("Are you satisfied with your changes? Please answer yes or no")
      if question3 == "no" :
        question1 = "yes"
      else : 
        break
       #Coloration des cercles modifiés
    
    x0=115
    x1=145
      #Remplissage premier cercle 
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess1, outline="black")
      #Remplissage deuxième cercle
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess2, outline="black")
      #Remplissage troisième cercle
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess3, outline="black")
      #Remplissage quatrième cercle
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill= guess4, outline="black")
  
    BonPlacement = 0
    BonneCouleur = 0
    if guess1 == circle1 : 
      BonPlacement += 1
    elif guess1 == circle2 :
      BonneCouleur +=1
    elif guess1 == circle3 : 
      BonneCouleur +=1 
    elif guess1 == circle4 : 
      BonneCouleur+=1
  
    if guess2 == circle2 : 
      BonPlacement += 1
    elif guess2 == circle1 :
      BonneCouleur +=1
    elif guess2 == circle3 : 
      BonneCouleur +=1 
    elif guess2 == circle4 : 
      BonneCouleur+=1
  
    if guess3 == circle3 : 
      BonPlacement += 1
    elif guess3 == circle1 :
      BonneCouleur +=1
    elif guess3 == circle2 : 
      BonneCouleur +=1 
    elif guess3 == circle4 : 
      BonneCouleur+=1
  
    if guess4 == circle4 : 
      BonPlacement += 1
    elif guess4 == circle1 :
      BonneCouleur +=1
    elif guess4 == circle2 : 
      BonneCouleur +=1 
    elif guess4 == circle3 : 
      BonneCouleur+=1

    #Remplissage des petis cercles
    y0_petit += 50
    y1_petit += 50
    x0=70
    x1=80
    for a in range(BonPlacement):
      x0 += 15
      x1 += 15
      canvas.create_oval(x0,y0_petit,x1,y1_petit, fill="red", outline="black")
    for z in range(BonneCouleur) : 
      x0 +=15 
      x1 += 15
      canvas.create_oval(x0,y0_petit, x1, y1_petit, fill = "white",outline="black")
  
    if BonPlacement == 4 : #Condition de fin de partie
      print("Congrats, you've won!")
      break 
      
    elif i == 9 and BonPlacement != 4 : #Condition de perte 
      print("Good try, but you've lost, the correct combination was", circle1, circle2, circle3, circle4 )
    else: 
          print("You have", BonPlacement, "guesses correct and", BonneCouleur,"good guesses of the colours used") 
          #Dans ce cas, faire apparaître les cercles rouges et blanc à côté par rapport au nombre de BonPlacement et BonneCouleur

def mode_1joueur ():
    """Fonction qui permet de jouer au Mastermind avec un mode de jeu de 1 seul joueur"""
    #Valeurs utilisés plus tard pour le remplissage des gros cercles
    y0= -15
    y1= 15
    #Valeurs utilisés plus tard pour le remplissage des petits cercles
    y0_petit=-4
    y1_petit= 6
  
    #Creation du code secret 
    cerclecode_1 = rd.randint(0,7)
    cerclecode_2 = rd.randint(0,7)
    cerclecode_3 = rd.randint(0,7)
    cerclecode_4 = rd.randint(0,7)

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

    print(cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4) #j'avais mis ça pour verifier les valeurs pour jouer 

    #Ce qui manque dans cette fonction c'est le remplissage des cercles au fur et à mesure des essais mais aussi la présence de petits cercles à côté de la rangé des cercles qu'on devinne au fur et à mesure
      
    #Creation de listes qu'on va remplir au fur et à mesure pour stocker les informations
    guesses_liste = []
    BonneCouleur_lise = []
    BonPlacement_liste = []
    
    for i in range(10) :
      guess1 = input("What colour is circle 1?")
      guess2 = input("What colour is circle 2?") 
      guess3 = input("What colour is circle 3?")
      guess4 = input("What colour is circle 4?")
      #faudrait remplir les cercles de i-ième essai avec les couleurs choisies (en soit ça devrait se faire avec cercle-i (fill = guess1) ) très grossièremen
      

      question1 = input("Do you want to change one or more guesses? Please answer yes or no")
      if question1 == "yes" : 
          question1_1 = int(input("How many guesses would you like to change?"))
          for k in range(question1_1) : 
            question2 = input("What guess would you like to change? Please answer as 'guess x' ")
            if question2 == "guess 1" : 
                guess1 = int(input("What colour is circle 1?"))
            elif question2 == "guess 2" : 
                guess2 = input("What colour is circle 2?")
            elif question2 == "guess 3" : 
                guess3 = input("what colour is circle 3?")
            elif question2 == "guess 4" : 
                guess4 = input("What colour is circle 4?")
      
      #Coloration du cercle 
      y0 += 50
      y1 += 50
      x0=115
      x1=145
      #Remplissage premier cercle 
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess1, outline="black")
      #Remplissage deuxième cercle
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess2, outline="black")
      #Remplissage troisième cercle
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess3, outline="black")
      #Remplissage quatrième cercle
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess4, outline="black")
      
      guesses_liste.append(guess1)
      guesses_liste.append(guess2)
      guesses_liste.append(guess3)
      guesses_liste.append(guess4)
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

      #Remplissage des petis cercles
      y0_petit += 50
      y1_petit += 50
      x0=70
      x1=80
      for a in range(BonPlacement):
        x0 += 15
        x1 += 15
        canvas.create_oval(x0,y0_petit,x1,y1_petit, fill="red", outline="black")
      for z in range(BonneCouleur) : 
        x0 +=15 
        x1 += 15
        canvas.create_oval(x0,y0_petit, x1, y1_petit, fill = "white",outline="black")
      

      if BonPlacement == 4 : 
        print("Congrats, you've won!")
        break
        
      elif i == 9 and BonPlacement != 4 : 
        print("Good try, but you've lost, the correcte combination was", cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4 )
        cercle01(fill = cerclecode_1)
        cercle02(fill = cerclecode_2)
        cercle03(fill = cerclecode_3)
        cercle04(fill = cerclecode_4)
      else: 
        print("You have", BonPlacement, "guesses correct and", BonneCouleur,"good guesses of the colours used")
        #Faut mettre à droite (ou à gauche, là où il y a la place quoi) des petits cercles indicatifs des essais. 
        #Donc faire apparaître "BonPlacement nombre" de petit cercle vert et "BonneCouleur nombre" de petit cercle jaune et faire en sorte que ces cercles restent fixe lors de la partie
        

def cacher_code():
    """Fonction qui permet au joueur qui fait deviner le code de le cacher"""
    canvas.itemconfigure(rectangle0, fill = "brown", outline="black")
    canvas.itemconfigure(cercle01, fill="brown", outline= "brown")
    canvas.itemconfigure(cercle02, fill="brown", outline= "brown")
    canvas.itemconfigure(cercle03, fill="brown", outline= "brown")
    canvas.itemconfigure(cercle04, fill="brown", outline= "brown")
    return


def decacher_code():
    canvas.itemconfigure(rectangle0, fill='grey')
    canvas.itemconfigure(cercle01, fill="white", outline= "black")
    canvas.itemconfigure(cercle02, fill="white", outline= "black")
    canvas.itemconfigure(cercle03, fill="white", outline= "black")
    canvas.itemconfigure(cercle04, fill="white", outline= "black")
    return

#création des widgets
mode = tk.LabelFrame(racine,text ="Mode de jeu", fg="black", bg= "grey80", highlightcolor="black") 

bouton_quitter = tk.Button(racine, text="Quitter", bg ="white", command = fermer_fenetre)
bouton_2joueurs = tk.Button(mode, text= "2 Joueurs", bg= "grey91", command = mode_2joueurs)
bouton_1joueur = tk.Button(mode, text= "1 Joueur", bg= "grey91", command = mode_1joueur)
bouton_cacher = tk.Button(racine, text = "Cacher", bg = "white", command = cacher_code)
bouton_decacher = tk.Button(racine, text = "Décacher", bg = "white", command = decacher_code)

# Position des widgets :
mode.grid (row=1, column=1, sticky='e')

bouton_quitter.grid(column=1, row=5)
bouton_2joueurs.grid(column=2, row=3, columnspan=2)
bouton_1joueur.grid(column=2, row=1, columnspan=2)
bouton_cacher.grid (column = 0, row = 4, columnspan=5, )
bouton_decacher.grid (column = 0, row = 5, columnspan=5)


### création des cerlces de couleur (haut)
cerclea = canvas.create_oval(170,5,185,20, fill='blue', outline="black")
cercleb = canvas.create_oval(190,5,205,20, fill='red', outline="black")
cerclec = canvas.create_oval(210,5,225,20, fill='orange', outline="black")
cercled = canvas.create_oval(230,5,245,20, fill='yellow', outline="black")
cerclee = canvas.create_oval(250,5,265,20, fill='green2', outline="black")
cerclef = canvas.create_oval(270,5,285,20, fill='turquoise', outline="black")
cercleg = canvas.create_oval(290,5,305,20, fill='violet', outline="black")
cercleh = canvas.create_oval(310,5,325,20, fill='pink', outline="black")

### création des rectangles
x0, x1 = 150, 350
y0= -20
y1 =20
for i in range (10):
  y0 += 50
  y1 +=50
  canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline="black")

rectangle0 = canvas.create_rectangle(150,560,350,600, fill = "grey", outline="black")

### création des cercles dans les rectangles
y0= -15
y1= 15
for j in range (1, 11):
  y0 += 50
  y1 += 50
  x0=115
  x1=145
  for i in range(1, 5):
    x0 += 50
    x1 += 50
    canvas.create_oval(x0,y0,x1,y1, fill="white", outline="black")

cercle01 = canvas.create_oval(165,565,195,595, fill='white', outline="black")
cercle02 = canvas.create_oval(215,565,245,595, fill='white', outline="black")
cercle03 = canvas.create_oval(265,565,295,595, fill='white', outline="black")
cercle04 = canvas.create_oval(315,565,345,595, fill='white', outline="black")

### création des cercles pour les points (à gauche)
y0=-4
y1= 6
for j in range (1, 11):
  y0 += 50
  y1 += 50
  x0=70
  x1=80
  for i in range(1, 5):
    x0 += 15
    x1 += 15
    canvas.create_oval(x0,y0,x1,y1, fill="grey", outline="black")
  

racine.mainloop()
