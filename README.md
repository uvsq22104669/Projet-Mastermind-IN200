# Projet-Mastermind-IN200
#Laurédane Coustillas
#Hippolyte Lefer
#Tilly Seassau
#Alexandre Schoumsky 
# https://github.com/uvsq22104669/Projet-Mastermind-IN200

############## 
### Le jeu
##############

Le mastermind est un jeu de stratégie où un joueur doit trouver une combinaison de 4 couleurs parmi 8, en 10 essais maximum. 
Dans un mode de jeu 1 joueur, c'est un ordinateur qui créer la combinaison et dans un mode de jeu avec 2 joueurs, le joueur A créer la combinaison et le joueur B la devine.

##########################
### Déroulement du jeu
##########################

Une fois la combinaison définie (par l'ordi ou par le joueur A), le joueur essaie de la deviner. Pour cela il place 4 pions dans la 1ère rangée.
Ensuite le joueur ou l'ordi doit déterminer s'il y a des pions de bonnes couleurs bien ou mal placés. Pour cela il utilise un code couleur. 
Un pion blanc signifie qu'un pion a la bonne couleur mais est mal placé. Un pion rouge signifie qu'un pion a la bonne couleur et est bien placé. 
L'absence de pion indique qu'il n'y a pas la couleur dans la combinaison secrète. Si au bout de 10 essais, le joueur n'a pas trouvé la combinaison, alors il a perdu.

##############################
## Fonctionnement du code
##############################

Dans un premier temps, nous avons créer une interface graphique tkinter qui modélise le jeu.
Nous avons fait une boucle pour dessiner les rectangles et les cercles ( chaque rectangle avec les 4 cercles représente un essai, sauf celui du bas qui sert pour la combinaison secrète). 
Les cercles de couleur en haut réprésentent les 8 couleurs existantes dans le jeu.
Nous avons créer des boutons pour les différents modes de jeux (1 joueur et 2 joueurs) ainsi que pour d'autres fonctionnalités comme cacher et décacher le code.

#########################
## Fonctions du code
#########################

Les fonctions mode de jeu 1 joueur et 2 joueurs sont similaires. Pour le mode 2 joueur, on demande au joueur A de définir une combinaison secrète de 4 pions (dans le mode 1 joueur, cela est automatiquement fait par l'ordinateur).
Ensuite, pour les 2 fonctions, on demande au joueur la couleur qu'il souhaite mettre dans chaque cercle puis s'il souaite la modifier.
Après chaque essai, l'ordi ou le joueur A détermine les pions bien et mal placés grâce à un code couleur.
Ici le code compare la couleur choisie par l'ordi/le joueur A et le joueur pour chaque cercle, avec 2 compteurs associés:
un pour les pions bien placés et un pour les pions mal placés. Une fois que le joueur a validé son essai, l'ordi/le joueur A détermine le nombre de pions bien et/ou mal placés. Une boucle permet de répéter cette opération pour chaque essai du joueur.
Si le joueur trouve la combinaison au bout de 10 essais (ou moins), il gagne, sinon il perd.

La fonction sauvegarde permet de sauvegarder une partie en cours, puis de la recharger avec le bouton recharger afin de permettre au joueur de conserver sa partie s'il n'a pas pu la finir.
