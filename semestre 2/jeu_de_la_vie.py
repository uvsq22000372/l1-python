####################################################
# Auteurs:
# Pierre Coucheney
# Toto
# Groupe:
# MPCI 2
# dépot Github:
# https://github.com/coucheney/jeudi_jeu_de_la_vie
###################################################

#########################
# import des modules

import tkinter as tk

##########################
# constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
LARGEUR = 600
HAUTEUR = 400
COTE = 10




########################
# fonctions

def quadrillage():
    '''Affiche un quadrillage constitué de carrés de côtés COTE'''
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += COTE


########################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)

# positionnement
canvas.grid()

# autres fonctions
quadrillage()


# boucle principal
racine.mainloop()