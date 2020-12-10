import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    canvas.create_line(i ,j, i+1, j, fill = color)

def ecran_aleatoire():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            color = get_color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            #print(ii, j, color)
            draw_pixel(i, j, color)

def degrade_gris():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            draw_pixel(i, j, get_color(i, i, i))

def degrade_2D():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            draw_pixel(i, j, get_color(i, 0, j))

root = tk.Tk()
root.title("tk")

bouton_aleatoire = tk.Button(root, command = ecran_aleatoire, text = "Aléatoire", font = ("helvetica", "15"), bg = "white", fg = "blue", relief = "groove", borderwidth = 1)
bouton_degrade_gris = tk.Button(root, command = degrade_gris, text = "Dégradé Gris", font = ("helvetica", "15"), bg = "white", fg = "blue", relief = "groove", borderwidth =1)
bouton_degrade_2D = tk.Button(root, command = degrade_2D, text = "Dégradé 2D", font = ("helvetica", "15"), bg = "white", fg = "blue", relief = "groove", borderwidth = 1)


bouton_aleatoire.grid(column = 0, row = 0)
bouton_degrade_gris.grid(column = 0, row = 1)
bouton_degrade_2D.grid(column = 0, row = 2)


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief = "raised", borderwidth = -2)
canvas.grid(column = 1, row = 0, rowspan = 3)


root.mainloop()