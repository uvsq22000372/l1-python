import tkinter as tk

cote = 50
pause = False

def bouton_pause():
    global pause
    if not pause:
        bouton.config(text="Restart")
        pause = True
    else:
        bouton.config(text="Pause")
        pause = False

def est_dans_carre(x, y):
    '''La fonction retourne True si le point de coordonnées (x, y) est dans le carré et False sinon'''
    inf = 250-cote//2
    sup = 250+cote//2
    return inf <= x <= sup and inf <= y <= sup 

def change_taille(event):
    global cote
    if not pause:
        if est_dans_carre(event.x, event.y) and cote >= 20:
            cote -= 10
            canvas.coords(carre, 250-cote//2, 250-cote//2, 250+cote//2, 250+cote//2)
        elif not est_dans_carre(event.x, event.y) and cote <= 100:
            cote += 10
            canvas.coords(carre, 250-cote//2, 250-cote//2, 250+cote//2, 250+cote//2)


racine = tk.Tk()
canvas = tk.Canvas(racine, bg="white", width=500, height=500)
canvas.grid(row=0, column=0)

bouton = tk.Button(racine, text="Pause", command=bouton_pause)
bouton.grid(row=1)

carre = canvas.create_rectangle((250-cote//2, 250-cote//2), (250+cote//2, 250+cote//2) , fill="red", outline="red")
canvas.bind("<Button-1>", change_taille)

racine.mainloop()