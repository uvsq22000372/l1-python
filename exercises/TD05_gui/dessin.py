import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

couleur = "blue"
objets = []

def dessineCercle():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    objets.append(canvas.create_oval(x, y, x+100, y+100, fill = couleur))


def dessineCarre():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    objets.append(canvas.create_rectangle(x, y, x+100, y+100, fill = couleur))

def dessineCroix():
    x = random.randint(0, CANVAS_WIDTH-100)
    y = random.randint(0, CANVAS_HEIGHT-100)
    objets.append(canvas.create_line(x, y+50, x+100, y+50, fill = couleur))
    objets.append(canvas.create_line(x+50, y, x+50, y+100, fill = couleur))
    
def choixCouleur():
    global couleur
    couleur = input ("Enter a color : ")

def undo():
    if (len(objets) != 0):
        if canvas.type(objets[-1]) == "line":
            canvas.delete(objets[-1])
            del objets[-1]
        canvas.delete(objets[-1])
        del objets[-1]
        
root = tk.Tk()
root.title("Mon dessin") #ajoute un titre

bouton_carre = tk.Button(root, text = "Carré", font = ("helvetica", "10"), command = dessineCarre, bg = "red", relief = "groove", borderwidth = 5)
bouton_cercle = tk.Button(root, text = "Cercle", font = ("helvetica", "10"), command = dessineCercle, bg = "blue", relief = "groove", borderwidth = 5)
bouton_croix = tk.Button(root, text = "Croix", font = ("helvetica", "10"), command = dessineCroix, bg = "yellow", relief = "groove", borderwidth = 5)
bouton_couleur = tk.Button(root, text = "Choisissez une couleur", font = ("helvetica", "10"), command = choixCouleur, cursor = "star")
bouton_undo = tk.Button(root, text = "Undo", font = ("helvetica", "10"), command = undo, bg = "yellow", relief = "groove", borderwidth = 5)

bouton_cercle.grid(column = 0, row = 1)
bouton_carre.grid(column = 0, row = 2)
bouton_croix.grid(column = 0, row = 3)
bouton_couleur.grid(column = 1, row = 0)
bouton_undo.grid(column = 2, row = 0)


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief = "raised", borderwidth = 5)
canvas.grid(column = 1, row = 1, rowspan = 3, columnspan = 2)

root.mainloop()