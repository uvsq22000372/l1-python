var_glob = 9
def division(var_loc) :
    var_loc = var_loc // var_glob
    return division

print (division)
   

def prog(argument):
    """ Multiplie par 4 l'argument puis soustrait 2 si l'argument
est supérieur à 1 et affiche -2 sinon"""
    if argument > 1:
        resultat = argument * 4
        resultat = resultat - 2
    else:
        print ("-2")

