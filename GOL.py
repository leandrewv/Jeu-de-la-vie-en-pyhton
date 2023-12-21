import random
from tkinter import *
# selection de la taille de la fenetre et sa largeur 
a  = int(input("Entrez la largeur de la fenêtre : "))
b = int(input("Entrez la hauteur de la fenêtre : "))

#Creation de la fenêtre
root = Tk()
canvas = Canvas(root, width = a, height =b, background="white")
canvas.pack()
#Creation du tableau
p = 40
n = 40
tableau = [[0 for _ in range(p)] for _ in range(n)]
jeu_en_cours = True #Markage pour reperer si le jeu est en cours


def verif_cellule_proche():
    new_tableau = [[0 for _ in range(p)] for _ in range(n)]# Crée une nouvelle liste nommée new_tableau de taille n par p remplie de zéros.
    for i in range(n):
        for j in range(p):# Effectue une double boucle pour parcourir chaque cellule du tableau.
            cpt = 0 # Initialise un compteur à 0.
            for k in [-1, 0, 1]:# Effectue une double boucle pour parcourir les cellules voisines de la cellule actuelle.
                for h in [-1, 0, 1]:# Si les indices k et h sont tous deux égaux à zéro, passe à la prochaine itération de la boucle intérieure.
                    if k == 0 and h == 0:
                        continue
                    nk = (i + k) % n
                    nh = (j + h) % p
                    if tableau[nk][nh] == 1:# Si la cellule voisine est vivante (valeur égale à 1), incrémente le compteur cpt.
                        cpt += 1
            if tableau[i][j] == 1 and 2 <= cpt <= 3:
                new_tableau[i][j] = 1 # Si la cellule actuelle est vivante et a 2 ou 3 cellules vivantes voisines, attribue 1 à la cellule correspondante dans le nouveau tableau new_tableau. Sinon, laisse la cellule du nouveau tableau à zéro.
            elif tableau[i][j] == 0 and cpt == 3: # Si la cellule actuelle est morte et a exactement 3 cellules vivantes voisines, attribue 1 à la cellule correspondante dans le nouveau tableau new_tableau.
                new_tableau[i][j] = 1
    return new_tableau # Retourne le nouveau tableau new_tableau contenant les mises à jour pour la prochaine génération du jeu.


def create_square_grid(): # Effectue une itération sur chaque cellule du tableau tableau et crée un rectangle.
    square_size = 15
    for i in range(n):
        for j in range(p):
            x1 = j * square_size
            y1 = i * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            if tableau[i][j] == 0:
                canvas.create_rectangle(x1, y1, x2, y2, outline="black")
            else:
                canvas.create_rectangle(x1, y1, x2, y2, fill="red")


def debut_jeu():# Effectue une double boucle pour parcourir chaque cellule du tableau tableau et, avec une probabilité de 0,1, attribue une valeur de 1 à la cellule, ce qui la rend vivante. Repetition du jeu avec la fonction verif_cellule_proche() jusqu'a ce que le jeu n'est plus en cours, grace au boutton stop.
    global jeu_en_cours #Dans le script donné, le mot-clé global est utilisé pour indiquer qu'une variable est une variable globale plutôt qu'une variable locale. Lorsqu'une variable est déclarée comme global, cela signifie qu'elle peut être accédée et modifiée depuis n'importe où dans le script, y compris à l'intérieur des fonctions.

    def base():
        for i in range(n):
            for j in range(p):
                if random.random() < 0.1:
                    tableau[i][j] = 1

        create_square_grid()
      
        def repition_grille():
            global jeu_en_cours, tableau
            if jeu_en_cours:
                tableau = verif_cellule_proche()
                canvas.delete("all")
                create_square_grid()
                if jeu_en_cours:
                    root.after(500, repition_grille)

        repition_grille()

    jeu_en_cours = True
    base()

# fontion pour mettre le jeu en pause 
def pause_jeu():
  global jeu_en_cours
  jeu_en_cours = False

# fontion pour reprendre le jeu
def continuer_jeu():
    global jeu_en_cours
    jeu_en_cours = True
    debut_jeu()

# fonction pour arreter le jeu et suprimer le tableau
def stop_jeu():
    global jeu_en_cours
    jeu_en_cours = False
    canvas.delete("all")

# Création des boutons
# bouton pour commencer le jeu
start_button = Button(root, text="Débuter", bg="blue", command=debut_jeu)
start_button.pack(side=LEFT)

# bouton pour mettre le jeu en pause
pause_button = Button(root, text="Pause ", bg="green", command=pause_jeu)
pause_button.pack(side=LEFT)

# bouton pour reprendre le jeu
resume_button = Button(root, text="Continuer", bg="cyan", command=continuer_jeu)
resume_button.pack(side=LEFT)

# bouton pour arreter le jeu
stop_button = Button(root, text="Stop", bg="red", command=stop_jeu)
stop_button.pack(side=LEFT)




root.mainloop()
