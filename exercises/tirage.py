import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

couleur = "blue"

used_numbers = []
num1 = random.randint(0, 50)


num4 = random.randint(0, 50)
num5 = random.randint(0, 50)

def numero1():
    canvas.create_text(CANVAS_WIDTH // 2 - 200, CANVAS_HEIGHT // 2, text = num1, fill = couleur, font = ("helvetica", "15"))
    used_numbers.append(num1)

def numero2():
    num2 = random.randint(0, 50)
    while num2 == num1 :
        num2 = random.randint(0, 50)
    canvas.create_text(CANVAS_WIDTH // 2 - 160, CANVAS_HEIGHT // 2, text = num2, fill = couleur, font = ("helvetica", "15"))
    used_numbers.append(num2)
num2 = used_numbers[1]

def numero3():
    num3 = random.randint(0, 50)
    while num2 == num1 or num2 == num2:
        num2 = random.randint(0, 50)
    canvas.create_text(CANVAS_WIDTH // 2 - 120, CANVAS_HEIGHT // 2, text = num3, fill = couleur, font = ("helvetica", "15"))
    used_numbers.append(num3)
    
def numero4():
    num4 = random.randint(0, 50)
    canvas.create_text(CANVAS_WIDTH // 2 - 80, CANVAS_HEIGHT // 2, text = num4, fill = couleur, font = ("helvetica", "15"))
    used_numbers.append(num4)

def numero5():
    num5 = random.randint(0, 50)
    canvas.create_text(CANVAS_WIDTH // 2 - 40, CANVAS_HEIGHT // 2, text = num5, fill = couleur, font = ("helvetica", "15"))
    used_numbers.append(num5)
    

root = tk.Tk()
root.title("EuroMillions") #ajoute un titre

bouton_num1 = tk.Button(root, text = "Numéro 1", font = ("helvetica", "10"), command = numero1, bg = "red", relief = "groove", borderwidth = 5)
bouton_num1.grid(column = 0, row = 0)

bouton_num2 = tk.Button(root, text = "Numéro 2", font = ("helvetica", "10"), command = numero2, bg = "red", relief = "groove", borderwidth = 5)
bouton_num2.grid(column = 0, row = 1)

bouton_num3 = tk.Button(root, text = "Numéro 3", font = ("helvetica", "10"), command = numero3, bg = "red", relief = "groove", borderwidth = 5)
bouton_num3.grid(column = 0, row = 2)

bouton_num4 = tk.Button(root, text = "Numéro 4", font = ("helvetica", "10"), command = numero4, bg = "red", relief = "groove", borderwidth = 5)
bouton_num4.grid(column = 0, row = 3)

bouton_num5 = tk.Button(root, text = "Numéro 5", font = ("helvetica", "10"), command = numero5, bg = "red", relief = "groove", borderwidth = 5)
bouton_num5.grid(column = 0, row = 4)


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "white", relief = "raised", borderwidth = 5)
canvas.grid(column = 1, row = 0, rowspan = 5)

root.mainloop()
print(used_numbers)