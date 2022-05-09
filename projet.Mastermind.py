# Groupe  LDDBI 5
# Laurédane COUSTILLAS
# Alexandre SCHOUMSKY
# Hippolyte LEFER
# Tilly SEASSAU
# https://github.com/uvsq22104669/Projet-Mastermind


#### Import des librairies
import tkinter as tk
import random as rd

#### Boucle principale
racine = tk.Tk()
racine.title("Mastermind")

#### Définition des constantes
CANVAS_WIDTH, CANVAS_HEIGHT = 400, 600

canvas = tk.Canvas(racine, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
canvas.grid(column=0, row=1)

#Variables utilisées pour la fonction Aide
guesses_liste = []
GuessListe = []
GuessInfo = []
GuessInfo_liste = []
color_list = ["blue","red", "orange", "yellow", "green", "turquoise", "violet", "pink"]

#### Fonctions
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
  
  #Valeurs utilisées plus tard pour la fonction aide
  #global guesses_liste 
  #global GuessListe
  #global GuessInfo
  #global GuessInfo_liste
  global inp
  
  #Cercle code 1
  lbl.config(text = "What is the colour of circle 1?")
  racine.wait_variable(inp)
  circlecode_1 = inp.get()
  inputtxt.delete(1.0, "end-1c")
  canvas.create_oval(165,565,195,595, fill= circlecode_1, outline="black")
  
  #Cercle code 2
  lbl.config(text = "What is the colour of circle 2?")
  racine.wait_variable(inp)
  circlecode_2 = inp.get()
  inputtxt.delete(1.0, "end-1c")
  canvas.create_oval(215,565,245,595, fill=circlecode_2, outline="black")
  
  #Cercle code 3
  lbl.config(text = "What is the colour of circle 3?")
  racine.wait_variable(inp)
  circlecode_3 = inp.get()
  inputtxt.delete(1.0, "end-1c")
  canvas.create_oval(265,565,295,595, fill=circlecode_3, outline="black")
  
  #Cercle code 4
  lbl.config(text = "What is the colour of circle 4?")
  racine.wait_variable(inp)
  circlecode_4 = inp.get()
  inputtxt.delete(1.0, "end-1c")
  canvas.create_oval(315,565,345,595, fill=circlecode_4, outline="black")

  lbl.config(text = "Do you want to change a circle? Please answer yes or no")
  racine.wait_variable(inp)
  question1 = inp.get()
  inputtxt.delete(1.0, "end-1c")
  while question1 == "yes" : 
      lbl.config(text = "What circle would you like to change? Please answer as 'circle x' ")
      racine.wait_variable(inp)
      question2 = inp.get()
      inputtxt.delete(1.0, "end-1c")
    
      if question2 == "circle 1" : 
        lbl.config(text = "What colour is circle 1 ?")
        racine.wait_variable(inp)
        circlecode_1 = inp.get()
        inputtxt.delete(1.0, "end-1c")
        canvas.create_oval(165,565,195,595, fill= circlecode_1, outline="black")
      elif question2 == "circle 2" : 
          lbl.config(text = "What colour is circle 2 ?")
          racine.wait_variable(inp)
          circlecode_2 = inp.get()
          inputtxt.delete(1.0, "end-1c")
          canvas.create_oval(215,565,245,595, fill=circlecode_2, outline="black")
      elif question2 == "circle 3" : 
          lbl.config(text = "What colour is circle 3 ?")
          racine.wait_variable(inp)
          circlecode_3 = inp.get()
          inputtxt.delete(1.0, "end-1c")
          canvas.create_oval(265,565,295,595, fill=circlecode_3, outline="black")               
      elif question2 == "circle 4" : 
        lbl.config(text = "What colour is circle 4 ?")
        racine.wait_variable(inp)
        circlecode_4 = inp.get()
        inputtxt.delete(1.0, "end-1c")
        canvas.create_oval(315,565,345,595, fill=circlecode_4, outline="black")
      lbl.config(text = "Do you want to change one or more circles?")
      racine.wait_variable(inp)
      question1 = inp.get()
      inputtxt.delete(1.0, "end-1c")
  
  lbl.config(text ="Cliquez sur 'Cacher' pour cacher votre code et permettre à votre adversaire de jouer")
   
  initial_guesses = ["", "", "", ""]
  
  for i in range(10) :
      guesses_liste = initial_guesses.copy()
      #Valeurs utilisées pour la creation de cercle
      y0 = -15 + 50 * (i + 1)
      y1 = 15 + 50 * (i + 1)
      for j in range(4):
        x0 = 115 + 50 * (j + 1)
        x1 = 145 + 50 * (j + 1)
        label_text = "What colour is circle " + str(j+1) +"?"
        lbl.config(text = label_text)
        #Boucle qui nous permet de rien mettre si c'est mal écrit
        while(guesses_liste[j] not in color_list): 
          racine.wait_variable(inp)
          guesses_liste[j] = inp.get()

        canvas.create_oval(x0,y0,x1,y1, fill= guesses_liste[j], outline="black")
        console_text = "Guess " + str(j+1) + " is"
        print(console_text, guesses_liste[j])
        inputtxt.delete(1.0, "end-1c")

      lbl.config(text = "Do you want to change one or more guesses? Please answer yes or anything else")
      racine.wait_variable(inp)
      change_guesses = inp.get()
      inputtxt.delete(1.0, "end-1c")
      
      while change_guesses == "yes" :   
          lbl.config(text = "What guess would you like to change? ")
          racine.wait_variable(inp)
          guess_id = inp.get()
          inputtxt.delete(1.0, "end-1c")
          while ((not guess_id.isdigit()) and int(guess_id) in range(1, 5)):
              lbl.config(text = "Please enter a valid integer")
              racine.wait_variable(inp)
              guess_id = inp.get()
              inputtxt.delete(1.0, "end-1c")

          circle_num = int(guess_id) - 1

          lbl.config(text = "What colour is circle " + guess_id + " ?")
          racine.wait_variable(inp)
          question3_text = inp.get()
          inputtxt.delete(1.0, "end-1c")
          guesses_liste[circle_num] = question3_text
          x0_temp = 115 + (circle_num+1) * 50
          x1_temp = 145 + (circle_num+1) * 50
          canvas.create_oval(x0_temp,
                               y0,
                               x1_temp,
                               y1,
                               fill = guesses_liste[circle_num],
                               outline = "black")
          lbl.config(text = "Do you want to change one or more guesses?")  
          racine.wait_variable(inp)
          change_guesses = inp.get()
          inputtxt.delete(1.0, "end-1c")
               
      GuessListe.append(guesses_liste)      
      BonPlacement = 0
      BonneCouleur = 0

      cerclecode_liste = [circlecode_1, circlecode_2, circlecode_3, circlecode_4]
      mauvaisecouleur_liste = []
      mauvaisguesses_liste = []
      for k in range(4):
        if guesses_liste[k] == cerclecode_liste[k]:
          BonPlacement += 1
        else:
          mauvaisecouleur_liste.append(cerclecode_liste[k])
          mauvaisguesses_liste.append(guesses_liste[k])

      for guess in mauvaisguesses_liste:
        if guess in mauvaisecouleur_liste:
          BonneCouleur += 1
          mauvaisecouleur_liste.remove(guess)

      for j in range(BonPlacement) : 
        GuessInfo.append("red")
      for k in range(BonneCouleur) : 
        GuessInfo.append("white")
      GuessInfo_liste.append(GuessInfo)

      #Remplissage des petis cercles
      y0_petit = -4 + 50 * (i + 1)
      y1_petit = 6 + 50 * (i + 1)

      x0_petit = 70
      x1_petit = 80
      
      for a in range(BonPlacement):
        x0_petit += 15
        x1_petit += 15
        canvas.create_oval(x0_petit,y0_petit,x1_petit,y1_petit, fill="red", outline="black")
      for z in range(BonneCouleur) : 
        x0_petit += 15 
        x1_petit += 15
        canvas.create_oval(x0_petit,y0_petit, x1_petit, y1_petit, fill ="white",outline="black")
      
      if BonPlacement == 4 : 
        lbl.config(text = "Congrats, you've won!")
        print("Congrats, you've won!")
        canvas.create_oval(165,565,195,595, fill= circlecode_1, outline="black")
        canvas.create_oval(215,565,245,595, fill= circlecode_2, outline="black")
        canvas.create_oval(265,565,295,595, fill= circlecode_3, outline="black")
        canvas.create_oval(315,565,345,595, fill= circlecode_4, outline="black")
        
      elif i == 9 and BonPlacement != 4 :
        lbl.config(text = "Good try, but you're out of guesses)
        print("Good try, but you've lost", circlecode_1, circlecode_2, circlecode_3, circlecode_4 )
        canvas.create_oval(165,565,195,595, fill= circlecode_1, outline="black")
        canvas.create_oval(215,565,245,595, fill= circlecode_2, outline="black")
        canvas.create_oval(265,565,295,595, fill= circlecode_3, outline="black")
        canvas.create_oval(315,565,345,595, fill= circlecode_4, outline="black")

      else: 
        print("You have", BonPlacement, "guesses correct and", BonneCouleur,"good guesses of the colours used")
            
def mode_1joueur ():
    """Fonction qui permet de jouer au Mastermind avec un mode de jeu de 1 seul joueur"""
    #Creation du code secret  
    cerclecode_1 = rd.choice(color_list)
    cerclecode_2 = rd.choice(color_list)
    cerclecode_3 = rd.choice(color_list)
    cerclecode_4 = rd.choice(color_list)

    print(cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4) # Pour vérifier si cela fonctionne 
      
    #Creation de listes qu'on va remplir au fur et à mesure pour stocker les informations
    #global guesses_liste 
    #global GuessListe
    #global GuessInfo
    #global GuessInfo_liste
    global inp
    initial_guesses = ["", "", "", ""]
  
    for i in range(10) :
      guesses_liste = initial_guesses.copy()
      #Valeurs utilisées pour la creation de cercle
      y0 = -15 + 50 * (i + 1)
      y1 = 15 + 50 * (i + 1)
      for j in range(4):
        x0 = 115 + 50 * (j + 1)
        x1 = 145 + 50 * (j + 1)
        label_text = "What colour is circle " + str(j+1) +"?"
        lbl.config(text = label_text)
        #Boucle qui nous permet de rien mettre si c'est mal écrit
        while(guesses_liste[j] not in color_list): 
          racine.wait_variable(inp)
          guesses_liste[j] = inp.get()

        canvas.create_oval(x0,y0,x1,y1, fill= guesses_liste[j], outline="black")
        console_text = "Guess " + str(j+1) + " is"
        print(console_text, guesses_liste[j])
        inputtxt.delete(1.0, "end-1c")

      lbl.config(text = "Do you want to change one or more guesses? Please answer yes or anything else")
      racine.wait_variable(inp)
      change_guesses = inp.get()
      inputtxt.delete(1.0, "end-1c")
      
      while change_guesses == "yes" :   
          lbl.config(text = "What guess would you like to change? ")
          racine.wait_variable(inp)
          guess_id = inp.get()
          inputtxt.delete(1.0, "end-1c")
          while ((not guess_id.isdigit()) and int(guess_id) in range(1, 5)):
              lbl.config(text = "Please enter a valid integer")
              racine.wait_variable(inp)
              guess_id = inp.get()
              inputtxt.delete(1.0, "end-1c")

          circle_num = int(guess_id) - 1

          lbl.config(text = "What colour is circle " + guess_id + " ?")
          racine.wait_variable(inp)
          question3_text = inp.get()
          inputtxt.delete(1.0, "end-1c")
          guesses_liste[circle_num] = question3_text
          x0_temp = 115 + (circle_num+1) * 50
          x1_temp = 145 + (circle_num+1) * 50
          canvas.create_oval(x0_temp,
                               y0,
                               x1_temp,
                               y1,
                               fill = guesses_liste[circle_num],
                               outline = "black")
          lbl.config(text = "Do you want to change one or more guesses?")  
          racine.wait_variable(inp)
          change_guesses = inp.get()
          inputtxt.delete(1.0, "end-1c")
               
      GuessListe.append(guesses_liste)      
      BonPlacement = 0
      BonneCouleur = 0

      cerclecode_liste = [cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4]
      mauvaisecouleur_liste = []
      mauvaisguesses_liste = []
      for k in range(4):
        if guesses_liste[k] == cerclecode_liste[k]:
          BonPlacement += 1
        else:
          mauvaisecouleur_liste.append(cerclecode_liste[k])
          mauvaisguesses_liste.append(guesses_liste[k])

      for guess in mauvaisguesses_liste:
        if guess in mauvaisecouleur_liste:
          BonneCouleur += 1
          mauvaisecouleur_liste.remove(guess)

      for j in range(BonPlacement) : 
        GuessInfo.append("red")
      for k in range(BonneCouleur) : 
        GuessInfo.append("white")
      GuessInfo_liste.append(GuessInfo)

      #Remplissage des petis cercles
      y0_petit = -4 + 50 * (i + 1)
      y1_petit = 6 + 50 * (i + 1)

      x0_petit = 70
      x1_petit = 80
      
      for a in range(BonPlacement):
        x0_petit += 15
        x1_petit += 15
        canvas.create_oval(x0_petit,y0_petit,x1_petit,y1_petit, fill="red", outline="black")
      for z in range(BonneCouleur) : 
        x0_petit += 15 
        x1_petit += 15
        canvas.create_oval(x0_petit,y0_petit, x1_petit, y1_petit, fill ="white",outline="black")
      
      if BonPlacement == 4 : 
        lbl.config(tetx = "Congrats, you've won!")
        print("Congrats, you've won!")
        canvas.create_oval(165,565,195,595, fill= cerclecode_1, outline="black")
        canvas.create_oval(215,565,245,595, fill= cerclecode_2, outline="black")
        canvas.create_oval(265,565,295,595, fill= cerclecode_3, outline="black")
        canvas.create_oval(315,565,345,595, fill= cerclecode_4, outline="black")
        
      elif i == 9 and BonPlacement != 4 : 
        lbl.config(text = "Good try, but you've lost")
        print("Good try, but you've lost, the correcte combination was", cerclecode_1, cerclecode_2, cerclecode_3, cerclecode_4 )
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
    """Fonction qui permet au joueur A de décacher le code"""
    canvas.itemconfigure(rectangle0, fill='grey')
    canvas.create_oval(165,565,195,595, fill= circle1, outline="black")
    canvas.create_oval(215,565,245,595, fill=circle2, outline="black")
    canvas.create_oval(265,565,295,595, fill=circle3, outline="black")
    canvas.create_oval(315,565,345,595, fill=circle4, outline="black")
    return

def valider ():
  """ Fonction qui permet de savoir à quel joueur c'est le tour de jouer: dès qu'un joueur a fini de jouer, le bouton
  change de couleur et détermine si c'est au joueur A ou B de jouer en fonction de la couleur"""
  for i in range(20):
    if bouton_valider["bg"] == "white":
        bouton_valider["bg"]="cyan"
  if bouton_valider["bg"] == "cyan":
        bouton_valider["bg"]="maroon1"  
  elif bouton_valider["bg"] == "maroon1":
        bouton_valider["bg"]="cyan"

def sauvegarde():
    """Sauvegarde la partie en cours dans un fichier sauvegarde.txt"""
    fic = open ("sauvegarde.txt", "w")
    fic.write ()
    pass
    fic.close()


def recharger():
    """Recharge le fichier sauvegarder pour continuer la partie en cours"""
    fic = open ("sauvegarde.txt", "r")
    pass
    canvas.delete()
                   
#Creation du Text Box
inputtxt = tk.Text(racine,height = 1, width = 15, bg = "white", fg = "black")
                   
#### Création des widgets
mode = tk.LabelFrame(racine,text ="Mode de jeu", fg="black", bg="grey80", highlightcolor="black") 
Joueur = tk.LabelFrame(racine, text="Joueur", fg="black", bg="grey80", highlightcolor="black")
JoueurA = tk.Label(Joueur, text="Joueur A", bg="cyan")
JoueurB = tk.Label(Joueur, text="Joueur B", bg="maroon1")
déco = tk.Label(racine, text="MASTERMIND", fg="black", font="Cambria", height="3")
lbl = tk.Label(racine, text = "Suivez les règles", bg = "white", fg = "black")
                   
#### Création des boutons
bouton_quitter = tk.Button(racine, text="Quitter", bg ="white", command= fermer_fenetre)
bouton_2joueurs = tk.Button(mode, text="2 Joueurs", bg="grey91", command= mode_2joueurs)
bouton_1joueur = tk.Button(mode, text="1 Joueur", bg="grey91", command= mode_1joueur)
bouton_cacher = tk.Button(racine, text="Cacher", bg="white", command= cacher_code)
bouton_decacher = tk.Button(racine, text ="Décacher", bg="white", command= decacher_code)
bouton_valider = tk.Button(racine, text="Valider", bg= "white", command= valider)
bouton_sauvegarder = tk.Button(racine, text="Sauvegarder", bg = "white", command = sauvegarde)
bouton_recharger = tk.Button(racine, text="Recharger", bg = "white", command = recharger)
                   

#### Position des widgets 
mode.grid (row=1, column=1, sticky='e')
Joueur.grid(row=0, column=1, sticky='ew')
JoueurA.grid(row=0, column=0)
JoueurB.grid(row=2, column=0)
déco.grid(row=0, column=0, columnspan=3)
lbl.grid(column = 0, row = 0, sticky = "NW")
inputtxt.grid(column = 0, row = 0, sticky = tk.W                   

#### Position des boutons
bouton_quitter.grid(column=1, row=5, sticky='se')
bouton_2joueurs.grid(column=2, row=3, columnspan=2)
bouton_1joueur.grid(column=2, row=1, columnspan=2)
bouton_cacher.grid(column=0, row=4, columnspan=5, )
bouton_decacher.grid(column=0, row=5, columnspan=5)
bouton_valider.grid(column=1, row=1, sticky='s')
bouton_sauvegarder.grid(column = 0, row = 1, sticky='sw')
bouton_recharger.grid(column = 0, row = 4, sticky='sw')
bouton_ok.grid(row = 1, column = 0, sticky = tk.NW)                   

#### Création des cerlces de couleur (haut)
cerclea = canvas.create_oval(170,5,185,20, fill='blue', outline="black")
cercleb = canvas.create_oval(190,5,205,20, fill='red', outline="black")
cerclec = canvas.create_oval(210,5,225,20, fill='orange', outline="black")
cercled = canvas.create_oval(230,5,245,20, fill='yellow', outline="black")
cerclee = canvas.create_oval(250,5,265,20, fill='green2', outline="black")
cerclef = canvas.create_oval(270,5,285,20, fill='turquoise', outline="black")
cercleg = canvas.create_oval(290,5,305,20, fill='violet', outline="black")
cercleh = canvas.create_oval(310,5,325,20, fill='pink', outline="black")

#### Création des rectangles
x0, x1 = 150, 350
y0 = -20
y1 = 20
for i in range (10):
  y0 += 50
  y1 += 50
  canvas.create_rectangle(x0,y0,x1,y1, fill = "grey", outline="black")

rectangle0 = canvas.create_rectangle(150,560,350,600, fill = "grey", outline="black")

#### Création des cercles dans les rectangles
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

#### Création des cercles pour les points (à gauche)
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
