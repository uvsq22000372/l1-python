import time

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jour, heure, minute, seconde = temps
    return ((jour*24 + heure)*60 + minute)*60 + seconde 


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60*60)
    seconde = seconde % (60*60)
    minute = seconde // 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)


temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


#fonction auxiliaire ici

def affiche_pluriel(valeur, mot) :
    if(valeur != 0) :
        print(valeur, " ",end="")
        print(mot,end="")
        if(valeur > 1):
            print("s", end="")
        print(", ", end=" ")


def afficheTemps(temps):
    affiche_pluriel(temps[0],"jour")
    affiche_pluriel(temps[1],"heure")
    affiche_pluriel(temps[2],"minute")
    affiche_pluriel(temps[3],"seconde")
    print
    
afficheTemps((1,0,14,23))    

def demandeTemps():
    jour = int(input("Entrer un nombre de jour"))
    heure = int(input("Entrez un nombre d'heures"))
    if(heure > 23):
        print("Nombre d'heures incorrect")
        return 
    minute = int(input("Entrez un nombre de minutes"))
    if (minute > 59) :
        print("Nombre de minutes incorrect")
        return
    seconde = int(input ("Entrez un nombre de secondes"))
    if (seconde > 59) :
        print("Nombre de secondes incorect")
        return
    return (jour, heure, minute, seconde)
     
#afficheTemps(demandeTemps())

#affiche temps

def sommeTemps(temps1,temps2):
    return secondeEnTemps(tempsEnSeconde(temps1) + tempsEnSeconde(temps2)) 


afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps ,proportion):
    return secondeEnTemps(proportion*tempsEnSeconde(temps))

afficheTemps(proportionTemps((2,0,36,0),0.2))
#appeler la fonction en échangeant l'ordre des arguments


def tempsEnDate(temps):
    jour, heure, minute, seconde = temps
    annee = 1970 + jour // 365
    jour = jour % 365
    return (annee, jour, heure, minute, seconde)

def afficheDate(date = -1):
    """ Affiche la date passée en argument, la date du jour si date = -1"""
    annee, jour, heure, minute, seconde = date
    affiche_pluriel(annee, "année")
    afficheDate((jour, heure, minute, seconde))
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))

print(time.time())
print(time.asctime(time.gmtime()))
afficheDate(tempsEnDate(secondeEnTemps(time.time())))

def estBisextile(annee):
    return (annee % 4 == 0) and (annee % 100 != 0) or annee % 400 == 0

def bisextile(jour):
    annee = 2020
    while jour > 0:
        if estBisextile(annee):
            jour -= 366
            print ("Est bisextile")
        else:
            jour -= 365
        annee +=1 


bisextile(20000)



import time

def nombreBisextile(jour):
    annee = 1970
    while jour > 0:
        if estBisextile(annee):
            jour -= 366
            print(annee, "est bisextile")
        else: 
            jour -= 365
        annee += 1
    return nombre_annee_bisextile

def tempsEnDateBisextile(temps):
    jour, heure, minute, seconde = seconde
    jour = jour - nombreBisextile(jour)
    annee = 1970 + jour // 365 
    jour = jour % 365
    return (annee, jour, heure, minute, seconde)

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))
print(time.asctime())
afficheDate(tempsEnDateBisextile(secondeEnTemps(time.time())))