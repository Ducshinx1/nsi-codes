def rechercher(a,tab):
    b = 0
    for i in range (len(tab)) :
        if a == tab[i] :
            b += 1
    return b 
            
        
pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):

    rendu = somme_versee
    a_rendre = somme_due
    i = len(pieces) - 1
    while not somme_versee == somme_due :
        if pieces[i] <= a_rendre :
            rendu.append([i])
            a_rendre = somme_due - somme_versee
        else :
            i = i - 1
    return rendu
