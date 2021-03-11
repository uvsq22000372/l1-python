import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

def recommencer():
    pass




root = tk.Tk()
root.title("Exercice 2")

bouton_pause = tk.Button(root, text = "Pause", font = ("helvetica", "10"), command = recommencer, bg = "red", relief = "groove", borderwidth = 5)
bouton_pause.grid(column = 0, row = 1)

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>")
canvas.grid(column = 0, row = 0)
root.mainloop()