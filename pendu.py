import numpy as np
import random

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
    Letter = input("quelle lettre choisissez vous?: ")
    while len(Letter) > 1:
        Letter = input("quelle lettre choisissez vous?: ")
    LetterExist = False
    
    if Letter in Mot:
        LetterExist = True
        
    for i in range(len(Mot)):
        if Mot[i] == Letter:
            MotHidden = MotHidden[:i] + Letter +MotHidden[i+1:]
            
    return MotHidden , LetterExist , Letter          


def Pendu(lstMots,nbChances):
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
            return True
        
        else:
            if essay[1] == True:
                print('Vrai, nombre de chances restantes: '+str(nbChances))
            else:
                nbChances -=1
                print('Faux, nombre de chances restantes: '+str(nbChances))
        


PenduGame = Pendu(mots, 20)

# word = ChooseWord(mots)
# Pendu = VerifyLetter(word[0],word[1])

