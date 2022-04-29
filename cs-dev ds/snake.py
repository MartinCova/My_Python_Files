import tkinter as tk
from random import randint
from tkinter.constants import LEFT, RIGHT, TOP

root = tk.Tk()
root.geometry('600x550')
root.resizable(None,None)

frametop = tk.Frame(root, height=100, width=600)
frametop.pack(side =TOP)

scoreLabel = tk.Label(frametop, text='Score')
scoreLabel.pack(side = LEFT)

exit_button = tk.Button(frametop, text="Quitter", command=root.destroy)
exit_button.pack(pady=30, side = RIGHT)

score = tk.StringVar()
scoreValue = tk.Entry(frametop, textvariable= score, state='disabled')
scoreValue.pack(side=RIGHT, pady= 30, padx= 50)

newgameButton = tk.Button(root, text='nouvelle partie', command = lambda: newGame())
newgameButton.pack(side = TOP)

canvas = tk.Canvas(bg = 'gray', height=400, width=600)
canvas.pack(side='bottom')

largeurSnake = 10
largeurpomme = 10

posx = 295
posy = 195

def newGame():
    """
    retourne en sortie la postion de départ du snake
    """
    canvas.delete("all")
    score.set("0")
    Pomme()
    canvas.bind('<Key>', Move)
    canvas.pack()
    snake = canvas.create_rectangle(posx,posy,posx+10,posy+10, fill='red')




def Move(event):
    global posx,posy
    touche = event.keysym
    if touche == 'a':
        posx += 50
    canvas.coords(snake,posx,posy,posx+10,posy+10)
        


class Pomme():
    """
    crée une pomme au hasard dans le canvas
    """
    def __init__(self) -> None:
        self.valx = randint(0,590)
        self.valy = randint(0,390)
        self.pomme = canvas.create_oval(self.valx,self.valy,self.valx+largeurpomme,self.valy+largeurpomme, fill = 'blue')



root.mainloop()