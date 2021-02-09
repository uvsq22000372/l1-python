import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

root = tk.Tk()
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "blue")
canvas.grid(column = 0, row = 0)

canvas.create_rectangle(CANVAS_WIDTH / 2 - 30, CANVAS_HEIGHT / 2 - 30, CANVAS_WIDTH / 2 + 30, CANVAS_HEIGHT / 2 + 30, fill = "yellow")

def pause():
     = "restart"


def clic(event):
    if (event.x == carre and event.y == carre and carre >= (20,20)):
        canvas.itemconfigure(carre, carre - 10, carre - 10)
    else:
        canvas.create_line(event.x, event.y, event.x + 10 , fill = "red")


bouton_pause = tk.Button(root, command = pause, text = "Pause")

bouton_pause.grid(column = 0, row = 1)

canvas.bind("<Button-1>", clic)

canvas.grid()
root.mainloop()