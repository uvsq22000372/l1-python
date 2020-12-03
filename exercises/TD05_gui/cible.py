import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 900, 900
nombre_cercles = 30

root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black", relief = "raised", borderwidth = 5)

liste_couleur = ["blue", "green", "black", "yellow", "magenta", "red"]




for i in range(nombre_cercles):
    canvas.create_oval(i*10, i*10, CANVAS_WIDTH - i*10, CANVAS_HEIGHT - i*10, fill = liste_couleur[i%6])

canvas.grid()
root.mainloop()