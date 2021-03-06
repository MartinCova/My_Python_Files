# Course hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc
#-------------------------------------------------------
import multiprocessing as mp
 
import os, time, math, random, sys, ctypes, signal

# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !

lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
                CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]


#-------------------------------------------------------
# La tache d'un cheval
def un_cheval(ma_ligne : int, keep_running,LONGEUR_COURSE,position,sem) : # ma_ligne commence à 0
    col=1

    while col < LONGEUR_COURSE and keep_running.value :
        sem.acquire()
        move_to(ma_ligne+1,col)         # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
        print('('+chr(ord('A')+ma_ligne)+'>')
        sem.release()

        col+=1
        position[ma_ligne] = col
        
        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1,5))
        finally :
            pass

def arbitre(position,Nb_process,sem,keep_running,LONGEUR_COURSE):
    gagnants =[]
    while keep_running.value == True:
        sem.acquire()
        position_copy = position[:]
        first = max(position_copy)

        last = min(position_copy)

        move_to(Nb_process+6,1)
        en_couleur(CL_WHITE)
        print('le premier est : (' + chr(ord('A') + position_copy.index(first)) + '>')
        print('le dernier est : (' + chr(ord('A') + position_copy.index(last)) + '>')
        sem.release()
        if max(position_copy) == LONGEUR_COURSE :
            for i in position_copy:
                #print(i)
                if i == LONGEUR_COURSE:
                    val = position_copy.index(i)
                    gagnants.append('(' + chr(ord('A') + val) + '>')
            move_to(Nb_process + 8, 1)
            print("le ou les gagnants sont: ")
            for i in gagnants:
                print(i)
            sys.exit(0)




#------------------------------------------------   
def prise_en_compte_signaux(signum, frame) :
    # On vient ici en cas de CTRL-C p. ex.
    move_to(Nb_process+11, 1)
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")
    
    for i in range(Nb_process): 
        mes_process[i].terminate() 
    
    move_to(Nb_process+12, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)
# ---------------------------------------------------
# La partie principale :
if __name__ == "__main__" :
    sem = mp.Lock()
    
    # Une liste de couleurs à affecter aléatoirement aux chevaux
    lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
                CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]
    
    LONGEUR_COURSE = 100 # Tout le monde aura la même copie (donc no need to have a 'value')
    
    keep_running=mp.Value(ctypes.c_bool, True)
    a = True
    Nb_process=10
    mes_process = [0 for i in range(Nb_process)]
    
    signal.signal(signal.SIGINT , prise_en_compte_signaux)
    signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()

    prono = input("quel va être le gagnant? : ")

    position = mp.Array('i', [0] * Nb_process)
    for i in range(Nb_process):  # Lancer     Nb_process  processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i,keep_running,LONGEUR_COURSE, position,sem))
        mes_process[i].start()

    pos = mp.Process(target=arbitre, args=(position, Nb_process,sem,keep_running,LONGEUR_COURSE))
    pos.start()

    move_to(Nb_process+10, 1)
    print("tous lancés, Controle-C pour tout arrêter")


    # On attend la fin de la course
    for i in range(Nb_process): mes_process[i].join()
    keep_running.value = False
    move_to(Nb_process+12, 1)
    curseur_visible()
    print("Fini")
