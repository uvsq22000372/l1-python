import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
nombre_clic = 0

def clic (event):
    global nombre_clic
    nombre_clic += 1
    if event.x < CANVAS_WIDTH - 100 and event.y < CANVAS_HEIGHT - 100:
        if nombre_clic % 2 == 0:
            canvas.create_rectangle(0, 0, CANVAS_HEIGHT - 100, CANVAS_WIDTH - 100, fill = "red")
        else:
            canvas.create_rectangle(0, 0, CANVAS_HEIGHT - 100, CANVAS_WIDTH - 100, fill = "blue")

def recommencer():
    nombre_clic == 0
    canvas.create_rectangle(0, 0, CANVAS_HEIGHT - 100, CANVAS_WIDTH - 100, fill = "red")

    
root = tk.Tk()
root.title("Exercice 1")

bouton_recommencer = tk.Button(root, text = "Recommencer", font = ("helvetica", "10"), command = recommencer, bg = "red", relief = "groove", borderwidth = 5)
bouton_recommencer.grid(column = 0, row = 1)

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>", clic)
canvas.create_rectangle(0, 0, CANVAS_HEIGHT - 100, CANVAS_WIDTH - 100, fill = "red")
canvas.grid(column = 0, row = 0)
root.mainloop()