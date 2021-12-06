
import random
import sys
import tkinter as tk
from library import malib
import PIL
# import malib


# created by Martin Cova on 12. nov. 2021
# objectif: créer un pendu sans interface gaphique

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
        


# ----------------------fenêtre graphique ----------------------

# def Begin_game():
#     FrameMenuEntry.place_forget()
#     play.place_forget()
#     quit.place_forget()
    
# from tkinter import PhotoImage, font as tkFont
# root= tk.Tk()

# screenX = root.winfo_screenwidth()
# screenY = root.winfo_screenheight()


# helv25 = tkFont.Font(family='Helvetica', size=25, weight='bold')

# root.geometry("800x600")
# root.title("Pendu")

# # -----------------création du menu principal d'entrée---------------------

# FrameMenuEntry = tk.Frame(root, width = screenX, height = screenY, bg = "#C8D6E5")
# FrameMenuEntry.place(x=0,y=0)

# ImagePendu = tk.Canvas(FrameMenuEntry,bg='blue', width= screenX, height= screenY/2)
# ImagePendu.place(x=0, y=0)

# bg = tk.PhotoImage(file='images\Lion-PNG-image-1.png')
# ImagePendu.create_image(0,0, image = bg)

# play = tk.Button(root, text='Jouer', bg='#54A0FF', fg='white',  font= helv25, command= lambda: Begin_game())
# play.place(relx=0.2 ,rely=0.7, relwidth=0.2)

# quit = tk.Button(root, text='Quitter', bg='#54A0FF', fg='white', font= helv25, command= lambda: root.destroy())
# quit.place(relx=0.6 , rely=0.7, relwidth=0.2)


# Frame1= tk.Canvas(root, width= screenX, height = 400, background="white")
# Frame2 = tk.Frame(root, width = screenX, height = 300, bg = "red")

# Frame2.place()



# root.mainloop()







PenduGame = Pendu(mots, 20)
