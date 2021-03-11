from random import sample, randrange
from tkinter import Tk, Canvas, Scale, Button, Label, N, ALL

COLORS=["ivory", "lime green", "red", "gray75"]

def random_forest(p, n):
    units=[(line,col) for col in range(n) for line in range(n)]
    ntrees=int(n**2*p)
    trees=sample(units,ntrees)
    states=[[0]*n for _ in range(n)]
    for (i,j) in trees:
        states[i][j]=1
    return states

def voisins(n, i, j):
    return [(a,b) for (a, b) in
            [(i, j+1),(i, j-1), (i-1, j), (i+1,j)]
            if a in range(n) and b in range(n)]

def fill_cell(states, line, col):
        A=(unit*col, unit*line)
        B=(unit*(col+1), unit*(line+1))
        state=states[line][col]
        color=COLORS[state]
        cnv.create_rectangle(A, B, fill=color, outline='')

def fill(states):
    n=len(states)
    for line in range(n):
        for col in range(n):
            fill_cell(states, line, col)

def update_states(states):
    n=len(states)
    to_fire=[]
    for line in range(n):
        for col in range(n):
            if states[line][col]==2:
                states[line][col]=3
                for (i, j) in voisins(n, line, col):
                    if states[i][j]==1:
                        to_fire.append((i, j))
    for (line,col) in to_fire:
        states[line][col]=2

def init():
    global states, cpt, ntrees, running

    p=int(curseur.get())/100
    running=False
    cpt=0
    lbl["text"]="%3s %%" %0
    curseur["state"]='normal'
    states=random_forest(p, n)
    ntrees=int(n*n*p)
    cnv.delete(ALL)
    fill(states)

def set_density(states, p):
    n=len(states)
    trees= [(i,j) for i in range(n) for j in range(n) if states[i][j]==1]
    nontrees=[(i,j) for i in range(n) for j in range(n) if states[i][j]!=1]
    density=len(trees)/n**2
    new_trees=int(n*n*p)
    before=len(trees)
    now=len(nontrees)
    delta=abs(new_trees-before)
    if new_trees>=before:
        for (i, j) in sample(nontrees, delta):
            states[i][j]=1
    else:
        for (i, j) in sample(trees, delta):
            states[i][j]=0

def make_forest(percent):
    global ntrees

    cnv.delete("all")
    p=float(percent)/100
    ntrees=int(n*n*p)
    set_density(states,p)
    fill(states)


def propagate():
    global cpt, running

    update_states(states)
    nfires=sum(states[i][j]==2 for i in range(n) for j in range(n))
    cpt+=nfires
    percent = int(cpt/ntrees*100)
    cnv.delete("all")
    fill(states)
    lbl["text"]="%3s %%" %percent
    if nfires==0:
        running=False
        return
    cnv.after(150, propagate)

def fire(event):
    global running, cpt

    i, j=event.y//unit, event.x//unit
    if states[i][j]==1:
        states[i][j]=2
        fill_cell(states, i, j)

        cpt+=1
        if not running:
            running=True
            curseur["state"]='disabled'
            propagate()

n=50
unit=10

# Fenêtre et canevas
root = Tk()
cnv = Canvas(root, width=unit*n-2, height=unit*n-2, background="ivory")
cnv.grid(row=0, column=0, rowspan=4)

btn=Button(root,text="New",  font='Arial 15 bold', command=init, width=8)
btn.grid(row=0, column=1, sticky=N)

lbl=Label(root,text="%3s %%" %0,  font='Arial 15 bold', bg='pink', width=5)
lbl.grid(row=2, column=1, sticky=N)

# Clic qui met le feu
cnv.bind("<Button-1>", fire)

curseur = Scale(root, orient = "vertical", command=make_forest, from_=100,
                to=0, length=200)
curseur.set(50)
curseur.grid(row=3, column=1)

init()

root.mainloop()