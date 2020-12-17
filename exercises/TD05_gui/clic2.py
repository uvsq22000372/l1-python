import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500

def drawCircle(event):
   
    if event.x > CANVAS_WIDTH // 2:
        canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill = "red")
    else:
         canvas.create_oval(event.x-25, event.y-25, event.x+25, event.y+25, fill = "blue")
    

root = tk.Tk()
root.title("Clic")


canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")
canvas.bind("<Button-1>", drawCircle)
canvas.create_line(CANVAS_WIDTH//2, 0, CANVAS_WIDTH/2, CANVAS_HEIGHT, fill = "white")
canvas.grid()
root.mainloop()