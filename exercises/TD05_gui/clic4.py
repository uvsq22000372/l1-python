import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
nombre_clic = 0

def drawCarre (event):
    global nombre_clic
    if nombre_clic == 10:
        root.destroy()
    else:
        nombre_clic += 1
        if nombre_clic % 2 == 0:
            canvas.create_rectangle(CANVAS_WIDTH / 2 - 25, CANVAS_HEIGHT / 2 - 25, CANVAS_WIDTH / 2 + 25, CANVAS_HEIGHT / 2 + 25, fill = "blue")
        else:
            canvas.create_rectangle(CANVAS_WIDTH / 2 - 25, CANVAS_HEIGHT / 2 - 25, CANVAS_WIDTH / 2 + 25, CANVAS_HEIGHT / 2 + 25, fill = "black")

root = tk.Tk()
root.title("Clic")


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>", drawCarre)

canvas.grid()
root.mainloop()