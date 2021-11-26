import os
import sys

def ReadDico(file):
    """ReadDico lis un dico
    
    Args:
        file (file): fichier à lire
    
    
    Returns:
        dic: dico des mots qu'on peut utiliser
    
    """
    f  = open(file, "r")
    dico = {}
    for x in f :
        y = x.replace(" ","").replace("\n","")
        z = y.split(":")
        dico[z[0]]=int(z[1])
    f.close()    
    return dico
    
transition = ( (1,8,8,8,4,8),
               (8,1,2,8,8,8),
               (8,2,8,3,8,8),
               (5,8,8,8,7,9),
               (8,8,8,3,8,8),
               (8,5,6,8,8,8),
               (8,6,8,8,8,9),
               (8,8,8,8,8,9))



def Automate(phrase):
    """Automate [summary]
    
    Args:
        phrase (str): phrase à traiter
        
    """
    dico = ReadDico("dico.txt")
    if '.' in phrase :
        phrase  = phrase[:-1] +' '+phrase[-1] 

    if '  .' in phrase:
        phrase  = phrase[:-2] +phrase[-1]
        
    place = 0

    if len(phrase) == 0:
        print("phrase incorrecte")
        exit(0)

    for i in phrase.split(" "):
        if not(i.lower() in dico.keys()):
            print("trouve d'autres mots, pas dans mon dico")
            return phrase
        mot_suiv  = dico.get(i.lower())
        place = transition[place][mot_suiv]
        if place == 8:
            print("phrase incorrect")
            # exit(0)
            return phrase
        elif place == 9:
            print("phrase correcte")
            # sys.exit()
            return phrase
    print('phrase incorrecte.')
    return phrase
    
# phrase =  

a = Automate(input("entrez votre phrase: "))

print(a)
