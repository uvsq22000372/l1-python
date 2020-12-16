import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 900, 600


root = tk.Tk()    #crée une fenêtre 

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x = CANVAS_WIDTH / 2
y0 = 100
y1 = CANVAS_HEIGHT - 100
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x - 50, y0 + 50, x + 50, y0 - 50)
canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
canvas.create_oval(x - 50, (y0 + y1)/2 + 50, x + 50, (y0+y1)/2 - 50)
    
    # Fin de votre code

canvas.grid()
root.mainloop()