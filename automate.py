import os
import sys

def ReadDico(file):
    f  = open("dico.txt", "r")
    dico = {}
    for x in f :
        print(x)
    


dico ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
                "mange" : 3, "petite" : 1, "joli" : 1, "grosse" : 1,
                "bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}


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
    if '.' in phrase :
        phrase  = phrase[:-1] +' '+phrase[-1] 
    place = 0

    if len(phrase) == 0:
        print("phrase incorrecte")
        exit(0)

    for i in phrase.split(" "):
        if not(i.lower() in dico.keys()):
            print("trouve d'autres mots, pas dans mon dico")
            exit(0)
        mot_suiv  = dico.get(i.lower())
        place = transition[place][mot_suiv]
        if place == 8:
            print("phrase incorrect")
            exit(0)
        elif place == 9:
            print("phrase correcte")
            sys.exit()
    print('phrase incorrecte.')
    
# phrase = input("entrez votre phrase: ")    

# a = Automate('Jean mange martin.')

b = ReadDico("dico.txt")