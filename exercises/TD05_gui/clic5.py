import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
nombre_clic = 0
liste_cercle = []

def drawCarre (event):
    global nombre_clic
    nombre_clic += 1
    if nombre_clic <= 8:
        liste_cercle.append(canvas.create_oval(event.x - 25, event.y - 25, event.x + 25, event.y + 25, fill = "red"))
    else:
        if nombre_clic == 9:
            for cercle in liste_cercle:
                canvas.itemconfigure(cercle, fill = "yellow")
        else:
            nombre_clic == 0
            for cercle in liste_cercle:
                canvas.delete(cercle)
            

root = tk.Tk()
root.title("Clic")


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>", drawCarre)

canvas.grid()
root.mainloop()