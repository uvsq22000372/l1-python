import tkinter as tk


CANVAS_WIDTH, CANVAS_HEIGHT = 100, 40

operande = 0
operande2 = 0
nombreplus = 0
nombremoins = 0
nombrefois = 0
nombredivise = 0

def rien():
    pass

def push_1():
    global operande
<<<<<<< HEAD
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 1
    else:
        operande2 = operande2*10 + 1
    Ecran.config(text = operande)

=======
    operande = operande*10 + 1
    Ecran.config(text = operande)
>>>>>>> cf354cb7e3883d30bc5522a9ba212fea05377561

def push_2():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 2
    else:
        operande2 = operande2*10 + 2
    Ecran.config(text = operande)


def push_3():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 3
    else:
        operande2 = operande2*10 + 3
    Ecran.config(text = operande)


def push_4():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 4
    else:
        operande2 = operande2*10 + 4
    Ecran.config(text = operande)


def push_5():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 5
    else:
        operande2 = operande2*10 + 5
def push_6():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 6
    else:
        operande2 = operande2*10 + 6
def push_7():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise

    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 7
    else:
        operande2 = operande2*10 + 7

def push_8():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise
    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 8
    else:
        operande2 = operande2*10 + 8

def push_9():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise
    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 9
    else:
        operande2 = operande2*10 + 9

def push_0():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise
    if nombreplus == 0 or nombremoins == 0 or nombrefois == 0 or nombredivise == 0:
        operande = operande*10 + 0
    else:
        operande2 = operande2*10 + 0

def plus():
    global operande
    global nombreplus
    nombreplus = operande

def moins():
    global operande
    global nombremoins
    nombremoins = operande

def fois():
    nombrefois = operande

def divise():
    nombredivise = operande

def egal():
    global operande
    global operande2
    global nombreplus
    global nombremoins
    global nombrefois
    global nombredivise
    if nombremoins != 0:
        operande = operande - operande2
        print (operande)


root = tk.Tk()

bouton_1 = tk.Button(root, text = "1", font = ("helvetica", "10"), width = 11, height = 7, command = push_1, bg = "red", relief = "groove")
bouton_1.grid(column = 0, row = 1)
bouton_2 = tk.Button(root, text = "2", font = ("helvetica", "10"), width = 11, height = 7, command = push_2, bg = "red", relief = "groove")
bouton_2.grid(column = 1, row = 1)
bouton_3 = tk.Button(root, text = "3", font = ("helvetica", "10"), width = 11, height = 7, command = push_3, bg = "red", relief = "groove")
bouton_3.grid(column = 2, row = 1)
bouton_4 = tk.Button(root, text = "4", font = ("helvetica", "10"), width = 11, height = 7, command = push_4, bg = "red", relief = "groove")
bouton_4.grid(column = 0, row = 2)
bouton_5 = tk.Button(root, text = "5", font = ("helvetica", "10"), width = 11, height = 7, command = push_5, bg = "red", relief = "groove")
bouton_5.grid(column = 1, row = 2)
bouton_6 = tk.Button(root, text = "6", font = ("helvetica", "10"), width = 11, height = 7, command = push_6, bg = "red", relief = "groove")
bouton_6.grid(column = 2, row = 2)
bouton_7 = tk.Button(root, text = "7", font = ("helvetica", "10"), width = 11, height = 7, command = push_7, bg = "red", relief = "groove")
bouton_7.grid(column = 0, row = 3)
bouton_8 = tk.Button(root, text = "8", font = ("helvetica", "10"), width = 11, height = 7, command = push_8, bg = "red", relief = "groove")
bouton_8.grid(column = 1, row = 3)
bouton_9 = tk.Button(root, text = "9", font = ("helvetica", "10"), width = 11, height = 7, command = push_9, bg = "red", relief = "groove")
bouton_9.grid(column = 2, row = 3)
bouton_0 = tk.Button(root, text = "0", font = ("helvetica", "10"), width = 11, height = 7, command = push_0, bg = "red", relief = "groove")
bouton_0.grid(column = 1, row = 4)
bouton_plus = tk.Button(root, text = "+", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_plus.grid(column = 3, row = 1)
<<<<<<< HEAD
bouton_moins = tk.Button(root, text = "-", font = ("helvetica", "10"), command = moins, bg = "red", relief = "groove")
=======
bouton_moins = tk.Button(root, text = "-", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
>>>>>>> cf354cb7e3883d30bc5522a9ba212fea05377561
bouton_moins.grid(column = 3, row = 2)
bouton_fois = tk.Button(root, text = "x", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_fois.grid(column = 3, row = 3)
bouton_divise = tk.Button(root, text = "/", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_divise.grid(column = 3, row = 4)
bouton_virgule = tk.Button(root, text = ",", font = ("helvetica", "10"), width = 11, height = 7, command = rien, bg = "red", relief = "groove")
bouton_virgule.grid(column = 2, row = 4)
<<<<<<< HEAD
bouton_egal = tk.Button(root, text = "=", font = ("helvetica", "10"), command = egal, bg = "red", relief = "groove")
bouton_egal.grid(column = 0, row = 4)

=======
>>>>>>> cf354cb7e3883d30bc5522a9ba212fea05377561
Ecran =tk.Label(root, text= "", font = ("helvetica", "10"), width = 48, height = 7,  bg = "white")
Ecran.grid(column = 0, row = 0, columnspan = 4)



root.mainloop()
