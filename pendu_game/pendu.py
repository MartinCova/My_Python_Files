
import random
import sys
# from tkinter.constants import INSERT
# from typing import Text
import tkinter as tk
from library import malib
import PIL

score = 0
MotCacheTkinter = 'gggghg'

# created by Martin Cova on 12. nov. 2021
# objectif: créer un pendu sans interface gaphique

mots = ['bonjour','merci', 'adieu', 'patate', 'tout']


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
        if i != Word[0]:
            WordHidden += '_'
        else:
            WordHidden += i
    print(Word)
    print(WordHidden)
    return Word , WordHidden


def VerifyLetter(Mot, MotHidden, letterused):
    """VerifyLetter vérifie si la lettre est dans le mot
    
    Args:
        Mot (str): mot en clair
        MotHidden (str): mot caché
    
    
    Returns:
        tuple: retourne le mot cahé(en partie découvert au sinon), un booléen si la lettre est dans le mot et de quelle lettre il s'agit
    
    """
    """vérification de la lettre entrée"""
    Letter = malib.IsText(input("Quelle lettre choisissez vous?: "))
    LetterExist = False

    while Letter in letterused:
        print("Lettre déjà utilisée, veuillez réesayer: ") 
        Letter = malib.IsText(input("Quelle lettre choisissez vous?: "))

    while len(Letter) > 1 :
        Letter = malib.IsText(input("Quelle lettre choisissez vous?: "))
   
    
 

    if Letter in Mot:
        LetterExist = True
        
    for i in range(len(Mot)):
        if Mot[i] == Letter:
            MotHidden = MotHidden[:i] + Letter +MotHidden[i+1:]
    
            
    return MotHidden , LetterExist , Letter          



def Pendu(lstMots,nbChances):
    """Pendu fonction principale du pendu
    
    Args:
        lstMots (liste): liste de mots random
        nbChances (int): nb de chances possible pour gagner
    
    """

    word = ChooseWord(lstMots)
    MotHidden = word[1]
    LetterUsed = []

    for i in range(nbChances):
        print(LetterUsed)
        essay = VerifyLetter(word[0], MotHidden, LetterUsed)
        MotHidden = essay[0]
        print(MotHidden)
        LetterUsed.append(essay[2])
        if MotHidden == word[0]:
            replay = malib.IsNumber(input('bravo vous avez gagné! Voulez-vous rejouer? 1:oui       2:non   :'))
            
            while replay != 1 and replay !=2:
                replay = malib.IsNumber(input('bravo vous avez gagné! Voulez-vous rejouer? 1:oui       2:non   :'))
              
            if replay == 2:
                break
            else:
                Pendu(lstMots, 8)
            
        else:
            if essay[1] == True:
                print('Vrai, nombre de chances restantes: '+str(nbChances))
            else:
                nbChances -=1
                print('Faux, nombre de chances restantes: '+str(nbChances))

    return nbChances




        

    



        
#PenduGame = Pendu(mots, 8)
#if PenduGame > score:
    score = PenduGame
#print('meilleur score = ', score)


# ----------------------fenêtre graphique ----------------------

def Begin_game():
    FrameMenuEntry.place_forget()
    play.place_forget()
    quit.place_forget()
    Pendu(mots, 8)
    InputZone.place(relwidth=0.4, relx= 0.1, rely = 0.5)


from tkinter import Label, PhotoImage, Variable, font as tkFont
root= tk.Tk()

screenX = root.winfo_screenwidth()
screenY = root.winfo_screenheight()

helv25 = tkFont.Font(family='Helvetica', size=25, weight='bold')

root.geometry("800x600")
root.title("Pendu")

# -----------------création du menu principal d'entrée---------------------

FrameMenuEntry = tk.Frame(root, width = screenX, height = screenY, bg = "#C8D6E5")
FrameMenuEntry.place(x=0,y=0)

#ImagePendu = tk.Canvas(FrameMenuEntry,bg='#C8D6E5', width= screenX, height= screenY/2)
#ImagePendu.place(x=0, y=0)



#bg = tk.PhotoImage(file='pendu_game/images/Lion-PNG-image-1.png')
#ImagePendu.create_image(0,0, image = bg)

play = tk.Button(root, text='Jouer', bg='#54A0FF', fg='white',  font= helv25, command= lambda: Begin_game())
play.place(relx=0.2 ,rely=0.7, relwidth=0.2)

quit = tk.Button(root, text='Quitter', bg='#54A0FF', fg='white', font= helv25, command= lambda: root.destroy())
quit.place(relx=0.6 , rely=0.7, relwidth=0.2)

#-----------------création de l'interface du jeu -----------------
entry  = tk.StringVar()
InputZone = tk.Entry(root,textvariable= entry)
InputZone.focus_set()

Word = tk.Label(root, text = MotCacheTkinter )
Word.place(relwidth = 0.5)




# Frame1= tk.Canvas(root, width= screenX, height = 400, background="white")
# Frame2 = tk.Frame(root, width = screenX, height = 300, bg = "red")

# Frame2.place()



root.mainloop()







