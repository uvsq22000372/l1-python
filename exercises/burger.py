import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


Burger = ['Five Guys', 'Burger King', 'McDonald_s', 'BàB', 'Frog', 'Steacknshake']

choix = random.choice(Burger)

def choix_burger():
    canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text = choix, fill = "red", font = ("helvetica", "15"))


root = tk.Tk()
root.title("Choix Burger")

bouton_choix_burger = tk.Button(root, text = "Choix Resto", font = ("helvetica", "10"), command = choix_burger, bg = "red", relief = "groove")
bouton_choix_burger.grid(column = 0, row = 0)


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white", relief = "raised", borderwidth = 5)
canvas.grid(column = 1, row = 0, rowspan = 1)

root.mainloop()
