import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

def drawPixel(event):
    canvas.create_line(event.x, event.y, event.x+1, event.y+1, fill = "red")


root = tk.Tk()
root.title("Clic")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>", drawPixel)



canvas.grid()
root.mainloop()