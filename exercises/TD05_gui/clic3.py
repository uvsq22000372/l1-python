import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
point1 = (0,0)
nombre_clic = 0

def drawLine (event):
    global point1
    global nombre_clic
    if nombre_clic == 0:
        point1 = (event.x, event.y)
        nombre_clic = 1
    else:
        nombre_clic = 0
        if (event.x <= CANVAS_WIDTH // 2 and point1[0] <= CANVAS_WIDTH // 2) or (event.x >= CANVAS_WIDTH // 2 and point1[0] >= CANVAS_WIDTH // 2):
            canvas.create_line(event.x, event.y, point1 , fill = "blue")
        else:
            canvas.create_line(event.x, event.y, point1 , fill = "red")
    
root = tk.Tk()
root.title("Clic")

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>", drawLine)
canvas.create_line(CANVAS_WIDTH//2, 0, CANVAS_WIDTH/2, CANVAS_HEIGHT, fill = "white")
canvas.grid()
root.mainloop()