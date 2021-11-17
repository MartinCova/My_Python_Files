
import random
import sys
import malib 

# created by Martin Cova on 12. nov. 2021
# object: créer un pendu sans interface gaphique

mots = ['bonjour','merci', 'adieu', 'patate']


def ChooseWord(lstMots):
    """ChooseWord fonction qui choisit un mot
    
    Args:
        lstMots (liste): liste de mots 
    
    
    Returns:
        str: mot choisit
    
    """
    Word  = random.choice(lstMots)
    WordHidden = ''
    for i in Word:
        WordHidden += '_'
    print(Word)
    # print(WordHidden)
    return Word , WordHidden


def VerifyLetter(Mot, MotHidden):
    """VerifyLetter vérifie si la lettre est dans le mot
    
    Args:
        Mot (str): mot en clair
        MotHidden (str): mot caché
    
    
    Returns:
        tuple: retourne le mot cahé(en partie découvert au sinon), un booléen si la lettre est dans le mot et de quelle lettre il s'agit
    
    """
    Letter = malib.IsText("Quelle lettre choisissez vous?: ")
    while len(Letter) > 1:
        malib.IsText("Quelle lettre choisissez vous?: ")
    LetterExist = False
    
    if Letter in Mot:
        LetterExist = True
        
    for i in range(len(Mot)):
        if Mot[i] == Letter:
            MotHidden = MotHidden[:i] + Letter +MotHidden[i+1:]
            
    return MotHidden , LetterExist , Letter          

def AffichagePendu(bool):
    potteaux = str('----------------\n|               |\n|               |\n|               \n|               \n|               \n|               \n|               \n|'
        '\n|               \n|               \n|               \n|               \n|---------------')
    
    tete = '() \n ()'
    
    print(potteaux, end = "")
    print(tete)






def Pendu(lstMots,nbChances):
    """Pendu fonction principale du pendu
    
    Args:
        lstMots (liste): liste de mots random
        nbChances (int): nb de chances possible pour gagner
    
    """
    LetterUsed = []
    word = ChooseWord(lstMots)
    MotHidden = word[1]
    for i in range(nbChances):
        print(LetterUsed)
        essay = VerifyLetter(word[0], MotHidden)
        MotHidden = essay[0]
        print(MotHidden)
        LetterUsed.append(essay[2])
        if MotHidden == word[0]:
            replay = malib.IsNumber('bravo vous avez gagné! Voulez-vous rejouer? 1:oui       2:non   :')
            while replay != 1 and replay !=2:
                replay = malib.IsNumber('bravo vous avez gagné! Voulez-vous rejouer? 1:oui       2:non   :')
              
            if replay == 2:
                sys.exit()
            else:
                Pendu(lstMots, malib.IsNumber("combien d'essais voulez-vous ?: "))
                
        
        else:
            if essay[1] == True:
                print('Vrai, nombre de chances restantes: '+str(nbChances))
            else:
                nbChances -=1
                print('Faux, nombre de chances restantes: '+str(nbChances))
        


# PenduGame = Pendu(mots, 20)


AffichagePendu(True)