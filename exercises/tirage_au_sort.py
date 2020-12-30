import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600


tirage = ["", "", "", ""]  #inscrire les éléments du tirage

choix1 = random.choice(tirage)
choix2 = random.choice(tirage), random.choice(tirage)
choix3 = random.choice(tirage), random.choice(tirage), random.choice(tirage)
choix4 = random.choice(tirage), random.choice(tirage), random.choice(tirage), random.choice(tirage)

def tirage_aleatoire1():
    canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 225, text = choix1, fill = "red", font = ("helvetica", "25"))

def tirage_aleatoire2():
    canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 75, text = choix2, fill = "red", font = ("helvetica", "25"))

def tirage_aleatoire3():
    canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 75, text = choix3, fill = "red", font = ("helvetica", "25"))

def tirage_aleatoire4():
    canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 + 225, text = choix4, fill = "red", font = ("helvetica", "25"))


root = tk.Tk()
root.title("Tirage au sort")

bouton_tirage_aleatoire1 = tk.Button(root, text = "Tirer un élément", font = ("helvetica", "10"), command = tirage_aleatoire1, bg = "red", relief = "groove")
bouton_tirage_aleatoire1.grid(column = 0, row = 0)
bouton_tirage_aleatoire2 = tk.Button(root, text = "Tirer deux éléments", font = ("helvetica", "10"), command = tirage_aleatoire2, bg = "red", relief = "groove")
bouton_tirage_aleatoire2.grid(column = 0, row = 1)
bouton_tirage_aleatoire3 = tk.Button(root, text = "Tirer trois éléments", font = ("helvetica", "10"), command = tirage_aleatoire3, bg = "red", relief = "groove")
bouton_tirage_aleatoire3.grid(column = 0, row = 2)
bouton_tirage_aleatoire4 = tk.Button(root, text = "Tirer quatre éléments", font = ("helvetica", "10"), command = tirage_aleatoire4, bg = "red", relief = "groove")
bouton_tirage_aleatoire4.grid(column = 0, row = 3)


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white", relief = "raised", borderwidth = 5)
canvas.grid(column = 4, row = 0, rowspan = 4)

root.mainloop()
