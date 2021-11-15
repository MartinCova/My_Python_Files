import math

# created by Martin Cova on 15. nov. 2021

mois = {'janvier':31, 'février':28, 'mars':31,'avril':30, 'mai':31, 'juin':30, 'juillet': 31, ' aout': 31, 'septembre': 30, 'octobre': 31, 'novembre': 30, 'décembre': 31}

def Bissextile(annee):
    b = str(annee)
    if b[-1] !=0 and b[-2] != 0 and annee % 4 == 0:
        return True 
    
    elif annee % 400 == 0:
        return True

    else:
        return False
    
    
a = Bissextile(int(input("choisissez votre année: ")))

print(a)


def JourMonth(année, mois):
    if mois == 'février': 
        print(mois.get("février"))       
    
