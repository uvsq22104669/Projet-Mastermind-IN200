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
  x0 = 115
  x1 = 145
  #Creation du code secret par un des joueurs 
  global circle1, circle2, circle3, circle4
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

  question1 = input("Do you want to change a circle? Please answer yes or no")
  while question1 == "yes" : 
      question2 = input("What circle would you like to change? Please answer as 'circle x' ")
      if question2 == "circle 1" : 
        circle1 = input("What colour is circle 1?")
        canvas.create_oval(165,565,195,595, fill= circle1, outline="black")
      elif question2 == "circle 2" : 
          circle2 = input("What colour is circle 2?")
          canvas.create_oval(215,565,245,595, fill=circle2, outline="black")
      elif question2 == "circle 3" : 
            circle3 = input("what colour is circle 3?")
            canvas.create_oval(265,565,295,595, fill=circle3, outline="black")               
      elif question2 == "circle 4" : 
            circle4 = input("What colour is circle 4?")
            canvas.create_oval(315,565,345,595, fill=circle4, outline="black")
      question1 = input("Do you want to change one or more circles?")
  
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
    
    x0=115
    x1=145
  
    question1 = input("Do you want to change a guesse? Please answer yes or no")
    while question1 == "yes" : 
          question2 = input("What guess would you like to change? Please answer as 'guess x' ")
          if question2 == "guess 1" : 
            guess1 = input("What colour is circle 1?")
            x0 += 50
            x1 += 50
            canvas.create_oval(x0,y0,x1,y1, fill= guess1, outline="black")
            x0 = 115
            x1 = 145
          elif question2 == "guess 2" : 
            guess2 = input("What colour is circle 2?")
            x0 +=100
            x1 +=100
            canvas.create_oval(x0,y0,x1,y1, fill = guess2, outline = "black")
            x0 = 115
            x1 = 145
          elif question2 == "guess 3" : 
            guess3 = input("what colour is circle 3?")
            x0 +=150
            x1 +=150
            canvas.create_oval(x0,y0,x1,y1, fill = guess3, outline = "black")
            x0 = 115
            x1 = 145                
          elif question2 == "guess 4" : 
            guess4 = input("What colour is circle 4?")
            x0 +=200
            x1 +=200
            canvas.create_oval(x0,y0,x1,y1, fill = guess4, outline = "black")
            x0 = 115
            x1 = 145
          question1 = input("Do you want to change one or more guesses?")
    
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
      canvas.create_oval(x0,y0_petit, x1, y1_petit, fill="white",outline="black")
  
    if BonPlacement == 4 : #Condition de fin de partie
      print("Congrats, you've won!")
      break 
      
    elif i == 9 and BonPlacement != 4 : #Condition de perte 
      print("Good try, but you've lost, the correct combination was", circle1, circle2, circle3, circle4 )
    else: 
          print("You have", BonPlacement, "guesses correct and", BonneCouleur,"good guesses of the colours used") 
            
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
      cerclecode_1 = "green2"
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
      cerclecode_2 = "green2"
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
      cerclecode_3 = "green2"
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
      cerclecode_4 = "green2"
    elif cerclecode_4 == 5 : 
      cerclecode_4 = "turquoise"
    elif cerclecode_4 == 6 : 
      cerclecode_4 = "violet"
    elif cerclecode_4 == 7 :
      cerclecode_4 = "pink"

    

    print(cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4) # Pour vérifier si cela fonctionne 
      
    #Creation de listes qu'on va remplir au fur et à mesure pour stocker les informations
    guesses_liste = []
    BonneCouleur_lise = []
    BonPlacement_liste = []
    
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
      guesses_liste.append(guess1)
      guess2 = input("What colour is circle 2?")
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess2, outline="black")
      guesses_liste.append(guess2)
      guess3 = input("What colour is circle 3?")
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess3, outline="black")
      guesses_liste.append(guess3)
      guess4 = input("What colour is circle 4?")
      x0 += 50
      x1 += 50
      canvas.create_oval(x0,y0,x1,y1, fill= guess4, outline="black")
      guesses_liste.append(guess4)
      x0=115
      x1=145

      question1 = input("Do you want to change one or more guesses? Please answer yes or no")
      while question1 == "yes" : 
          question1_1 = int(input("How many guesses would you like to change?"))
          for k in range(question1_1) : 
            question2 = input("What guess would you like to change? Please answer as 'guess x' ")
            if question2 == "guess 1" : 
                guess1 = input("What colour is circle 1?")
                x0 += 50
                x1 += 50
                canvas.create_oval(x0,y0,x1,y1, fill= guess1, outline="black")
                x0 = 115
                x1 = 145
            elif question2 == "guess 2" : 
                guess2 = input("What colour is circle 2?")
                x0 +=100
                x1 +=100
                canvas.create_oval(x0,y0,x1,y1, fill = guess2, outline = "black")
                x0 = 115
                x1 = 145
            elif question2 == "guess 3" : 
                guess3 = input("what colour is circle 3?")
                x0 +=150
                x1 +=150
                canvas.create_oval(x0,y0,x1,y1, fill = guess3, outline = "black")
                x0 = 115
                x1 = 145                
            elif question2 == "guess 4" : 
                guess4 = input("What colour is circle 4?")
                x0 +=200
                x1 +=200
                canvas.create_oval(x0,y0,x1,y1, fill = guess4, outline = "black")
          question1 = input("Do you want to change one or more guesses?")
      
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
        canvas.create_oval(x0,y0_petit, x1, y1_petit, fill ="white",outline="black")
      

      if BonPlacement == 4 : 
        print("Congrats, you've won!")
        canvas.create_oval(165,565,195,595, fill= cerclecode_1, outline="black")
        canvas.create_oval(215,565,245,595, fill= cerclecode_2, outline="black")
        canvas.create_oval(265,565,295,595, fill= cerclecode_3, outline="black")
        canvas.create_oval(315,565,345,595, fill= cerclecode_4, outline="black")
        break

        
      elif i == 9 and BonPlacement != 4 : 
        print("Good try, but you've lost, the correcte combination was", cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4 )
        cercle01(fill = cerclecode_1)
        cercle02(fill = cerclecode_2)
        cercle03(fill = cerclecode_3)
        cercle04(fill = cerclecode_4)
        canvas.create_oval(165,565,195,595, fill= cerclecode_1, outline="black")
        canvas.create_oval(215,565,245,595, fill= cerclecode_2, outline="black")
        canvas.create_oval(265,565,295,595, fill= cerclecode_3, outline="black")
        canvas.create_oval(315,565,345,595, fill= cerclecode_4, outline="black")

      else: 
        print("You have", BonPlacement, "guesses correct and", BonneCouleur,"good guesses of the colours used")
       
def cacher_code():
    """Fonction qui permet au joueur qui fait deviner le code de le cacher"""
    canvas.itemconfigure(rectangle0, fill = "brown")
    canvas.create_oval(165,565,195,595, fill='brown', outline="brown")
    canvas.create_oval(215,565,245,595, fill='brown', outline="brown")
    canvas.create_oval(265,565,295,595, fill='brown', outline="brown")
    canvas.create_oval(315,565,345,595, fill='brown', outline="brown")
    return


def decacher_code():
    canvas.itemconfigure(rectangle0, fill='grey')
    canvas.create_oval(165,565,195,595, fill= circle1, outline="black")
    canvas.create_oval(215,565,245,595, fill=circle2, outline="black")
    canvas.create_oval(265,565,295,595, fill=circle3, outline="black")
    canvas.create_oval(315,565,345,595, fill=circle4, outline="black")
    return

def valider ():
  for i in range(20):
    if bouton_valider["bg"] == "white":
        bouton_valider["bg"]="cyan"
  if bouton_valider["bg"] == "cyan":
        bouton_valider["bg"]="maroon1"  
  elif bouton_valider["bg"] == "maroon1":
        bouton_valider["bg"]="cyan"
        
# Création des widgets
mode = tk.LabelFrame(racine,text ="Mode de jeu", fg="black", bg="grey80", highlightcolor="black") 
Joueur = tk.LabelFrame(racine, text="Joueur", fg="black", bg="grey80", highlightcolor="black")
JoueurA = tk.Label(Joueur, text="Joueur A", bg="cyan")
JoueurB = tk.Label(Joueur, text="Joueur B", bg="maroon1")
déco = tk.Label(racine, text="MASTERMIND", fg="black", font="Cambria", height="3")
# Création des boutons

bouton_quitter = tk.Button(racine, text="Quitter", bg ="white", command= fermer_fenetre)
bouton_2joueurs = tk.Button(mode, text="2 Joueurs", bg="grey91", command= mode_2joueurs)
bouton_1joueur = tk.Button(mode, text="1 Joueur", bg="grey91", command= mode_1joueur)
bouton_cacher = tk.Button(racine, text="Cacher", bg="white", command= cacher_code)
bouton_decacher = tk.Button(racine, text ="Décacher", bg="white", command= decacher_code)
bouton_valider = tk.Button(racine, text="Valider", bg= "white", command= valider)

# Position des widgets 

mode.grid (row=1, column=1, sticky='e')
Joueur.grid(row=0, column=1, sticky='ew')
JoueurA.grid(row=0, column=0)
JoueurB.grid(row=2, column=0)
déco.grid(row=0, column=0, columnspan=3)

# Position des boutons
bouton_quitter.grid(column=1, row=5, sticky='se')
bouton_2joueurs.grid(column=2, row=3, columnspan=2)
bouton_1joueur.grid(column=2, row=1, columnspan=2)
bouton_cacher.grid(column=0, row=4, columnspan=5, )
bouton_decacher.grid(column=0, row=5, columnspan=5)
bouton_valider.grid(column=1, row=1, sticky='s')


### Création des cerlces de couleur (haut)
cerclea = canvas.create_oval(170,5,185,20, fill='blue', outline="black")
cercleb = canvas.create_oval(190,5,205,20, fill='red', outline="black")
cerclec = canvas.create_oval(210,5,225,20, fill='orange', outline="black")
cercled = canvas.create_oval(230,5,245,20, fill='yellow', outline="black")
cerclee = canvas.create_oval(250,5,265,20, fill='green2', outline="black")
cerclef = canvas.create_oval(270,5,285,20, fill='turquoise', outline="black")
cercleg = canvas.create_oval(290,5,305,20, fill='violet', outline="black")
cercleh = canvas.create_oval(310,5,325,20, fill='pink', outline="black")

### Création des rectangles
x0, x1 = 150, 350
y0 = -20
y1 = 20
for i in range (10):
  y0 += 50
  y1 += 50
  canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline="black")

rectangle0 = canvas.create_rectangle(150,560,350,600, fill = "grey", outline="black")

### Création des cercles dans les rectangles
y0 = -15
y1 = 15
for j in range (1, 11):
  y0 += 50
  y1 += 50
  x0 = 115
  x1 = 145
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
  

N=100
config_cur = None
def sauvegarde():
    """Sauvegarde la config courante dans le fichier sauvegarde"""
    fic = open("sauvegarde", "w")
    fic.write(str(N)+"\n")
    for i in range(1, N+1):
        for j in range(1, N+1):
            fic.write(str(config_cur[i][j]))
            fic.write("\n")
    fic.close()
bouton_sauvegarder = tk.Button(racine, text="Sauvegarder", bg = "white", command = sauvegarde)
bouton_sauvegarder.grid(column = 0, row = 1, sticky='sw')


def load():
    """Charge la configuration sauvegardée et la retourne si
    elle a même valeur N que la config courante, sinon retourne config vide
    """
    fic = open("sauvegarde", "r")
    config = [[0 for i in range(N+2)] for j in range(N+2)]
    ligne = fic.readline()
    n = int(ligne)
    if n != N:
        fic.close()
        return config
    i = j = 1
    for ligne in fic:
        config[i][j] = int(ligne)
        j += 1
        if j == N + 1:
            j = 1
            i += 1
    fic.close()
    return config

bouton_recharger = tk.Button(racine, text="Recharger", bg = "white", command = load)
bouton_recharger.grid(column = 0, row = 4, sticky='sw')

racine.mainloop()
