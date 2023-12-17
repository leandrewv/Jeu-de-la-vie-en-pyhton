import random
from tkinter import *

root = Tk()
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

p = 40
n = 40
tableau = [[0 for _ in range(p)] for _ in range(n)]


def verif_cellule_proche():
    new_tableau = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            cpt = 0
            for k in [-1, 0, 1]:
                for h in [-1, 0, 1]:
                    if k == 0 and h == 0:
                        continue
                    nk = (i + k) % n
                    nh = (j + h) % p
                    if tableau[nk][nh] == 1:
                        cpt += 1
            if tableau[i][j] == 1 and 2 <= cpt <= 3:
                new_tableau[i][j] = 1
            elif tableau[i][j] == 0 and cpt == 3:
                new_tableau[i][j] = 1
    return new_tableau


def create_square_grid():
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


def base():
    for i in range(n):
        for j in range(p):
            if random.random() < 0.1:  
                tableau[i][j] = 1

    create_square_grid()

    def update_grid():
        global tableau
        tableau = verif_cellule_proche()
        canvas.delete("all")
        create_square_grid()
        root.after(100, update_grid)

    update_grid()


base()
root.mainloop()
