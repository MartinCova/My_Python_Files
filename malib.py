from functools import cmp_to_key
import math

# created by Martin Cova on 15. nov. 2021

# ---------------Exercie 1-----------------

Month = {'janvier':31, 'février':28, 'mars':31,'avril':30, 'mai':31, 'juin':30, 'juillet': 31, ' aout': 31, 'septembre': 30, 'octobre': 31, 'novembre': 30, 'décembre': 31}

def Bissextile(annee):
    """Bissextile fonction qui dit si une année est bissextile ou non 
    
    Args:
        annee (int): année
    
    
    Returns:
        [bool]: année bissextile ou non 
    
    """
    b = str(annee)
    if b[-1] !=0 and b[-2] != 0 and annee % 4 == 0:
        return True 
    
    elif annee % 400 == 0:
        return True

    else:
        return False
    
    

def JourMonth(annee, mois):
    """JourMonth fonction qui donne le nb de jours dans un mois
    
    Args:
        annee (int): [année]
        mois (str): [mois]
    
    
    Returns:
        [number]: [nb de jours dans le mois]
    
    """
    if mois == 'février':
        if Bissextile(annee)==True:
            return 29
        else:
            return Month.get("février")
    else:
        return Month.get(mois)
     


def DayExist(annee, month, day):
    """DayExist fonction qui valide l'existence d'un jour ou non 

    Args:
        annee (int): année
        month (str): mois
        day (int): jour
    
    
    Returns:
        bool: existe ou pas
    
    """
    if day  > 31 :
        return False
    if day < 0:
        return False
    if month == 'février' and Bissextile(annee) == True:
        if day > Month.get(month)+1:
            return False
        else:
            return True
    elif day <= Month.get(month):
        return True
    else:
        return False
            

def mesImpots(revenu):
    """mesImpots calcule le montant des impots du revenu rentré
    
    Args:
        revenu (number): montant des revenus à calculer 
    
    
    Returns:
        [number]: montant des imôts à payer
    
    """
    impot = 0
    if revenu > 158123:
        impot  = (revenu - 15823)*45/100 + (158122 - 73517)*41/100 +(73516 - 25711)*30/100 + (25710 - 10085)*11/100 
    elif revenu >= 73517:
        impot = (revenu - 73517)*41/100 +(73516 - 25711)*30/100 + (25710 - 10085)*11/100
    elif revenu >= 25711:
        impot = (revenu - 25711)*30/100 + (25710 - 10085)*11/100
    elif revenu >= 1085:
        impot = (revenu - 10085)*11/100
    return impot
        

def multiplication(mat1,mat2):
    """multiplication multiplie deux matrices
    
    Args:
        mat1 (liste): matrice1
        mat2 (liste): matrice2
    
    
    Returns:
        liste: produit des deux matrices
    
    """
    prod = [[0 for i in range(len(mat1[0]))] for j in range(len(mat2))]
    if len(mat1[0]) != len(mat2):
        print('impossible de calculer le produit de ces deux matrices')
    else:
        somme = 0
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2[0])):
                    prod[i][j]+= mat1[i][k]*mat2[k][j]
    return prod


def AffichageMatrice(prod):
    """AffichageMatrice affiche la matrice calculée
    
    Args:
        prod (liste): matrice
    
    """
    for i in range(len(prod)):
        print(prod[i])
        
            


def Syracuse(n,it):
    """Syracuse suite de syracuse
    
    Args:
        n (entier): nb de départ
        it (entier): nb d'itération
    
    
    Returns:
        liste: liste de la suite de syracuse
    
    """
    lst = []
    if n < 0:
        return False
    if type(n) != int:
        return False
    for i in range(it):
        if n % 2 == 0:
            # print(n)
            lst.append(n)
            n = n/2
        else:
            # print(n)
            lst.append(n)
            n = 3*n +1
        
    return lst 
        
     
def Altitude(suite):
    """Altitude calcule l'altitude d'une suite de syracuse
    
    Args:
        suite (liste): suite de syracuse à calculer l'altitude
    
    
    Returns:
        int: nb max que la suite atteint
    
    """
    max = 0
    for i in range(len(suite)):
        if suite[i]> max:
            max = suite[i]
    return max
            

def TimeFlight(suite):
    """TimeFlight calc temps de vol d'une suite de syracuse
    
    Args:
        suite (liste): liste à calculer le temps de vol
    
    
    Returns:
        entier: rang à partir duquel l'itération 142 commence
    
    """
    for i in range(len(suite)):
        if suite[i] == 1 and suite[i+1] == 4 and suite[i+2] == 2:
            return i
        

def BooleenneTricolore(n):
    nbcarre = str(n**2)
    print(nbcarre)
    for i in nbcarre:
        if not(i in '149'):
            print("le nombre n'est pas tricolore")
            return False
    print('le nombre est tricolore')
    

def Hanoi(n,d,i,f):
    if n>0:
        Hanoi(n-1,d,f,i)
        print('deplacer le disque du plot',d, 'vers le plot',f)
        
        Hanoi(n-1,i,d,f)
