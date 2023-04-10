# Martin COVA et Hugues FARTHOUAT

# Cours hippique
# Version tres basique, sans mutex sur l'ecran, sans arbitre, sans annoncer le gagant, ... ...

# Quelques codes d'echappement (tous ne sont pas utilises)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer apres la position du curseur
CRLF  = "\r\n"                     #  Retour e la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# Actions sur les caracteres affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligne


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
CL_DARKGRAY="\033[01;30m"               #  Gris fonce
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc
#-------------------------------------------------------
import multiprocessing as mp
import os, time,math, random, sys, ctypes, signal

# Definition de qq fonctions de gestion de l'ecran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def erase_line() : print("\033[K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !

#-------------------------------------------------------
# La tache d'un cheval
def un_cheval(ma_ligne : int, keep_running,pos,first,lock, LONGEUR_COURSE, poule, compte, lyst_colors) : # ma_ligne commence e 0
    col=1
    anim = 0
    while col < LONGEUR_COURSE and keep_running.value :
        lock.acquire()
        pos[ma_ligne] = col
        # Poule
        if poule:
            move_to(ma_ligne*compte+1,col)
            erase_line_from_beg_to_curs()
            erase_line()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print((anim%3*" ")+"   \\\\")

            move_to(ma_ligne*compte+2,col)
            erase_line_from_beg_to_curs()
            erase_line()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print((anim%3*" ") + "   (o>")

            move_to(ma_ligne*compte+3,col)
            erase_line_from_beg_to_curs()
            erase_line()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print("\\\\"+chr(ord('A')+ma_ligne)+"//)")

            move_to(ma_ligne*compte+4,col)
            erase_line_from_beg_to_curs()
            erase_line()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print(" \\_/_)")

            move_to(ma_ligne*compte+5,col)
            erase_line()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print("  \\|_" if anim == 1 else "  _|_" if anim == 2 else "  _|/" if anim == 3 else "  _|_")
        else:
            # Cheval
            move_to(ma_ligne*compte+1,col)
            erase_line_from_beg_to_curs()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print("  _____/\\")
            move_to(ma_ligne*compte+2,col)
            erase_line_from_beg_to_curs()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print("/|__"+chr(ord('A')+ma_ligne)+"__/")
            move_to(ma_ligne*compte+3,col)
            erase_line_from_beg_to_curs()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            print(" /\\   /\\")
        # print('('+chr(ord('A')+ma_ligne)+'>')
        lock.release()
        col+=1
        anim = 1 + anim%4
        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1, 5))
        finally :
            pass
    for i in range(Nb_process):
        if(first[i] == ""):
            first[i] = chr(ord('A')+ma_ligne)
            return

def arbitre(ma_ligne : int, keep_running,pos,first,pari,lock, LONGEUR_COURSE, poule) :
    col=1
    while col < LONGEUR_COURSE and keep_running.value :
        lock.acquire()
        max_lines = []
        min_lines = []
        max = 0
        min = 99999
        for i in range(len(pos)):
            if pos[i] < min:
                min = pos[i]
                min_lines.clear()
                min_lines.append(chr(ord('A')+i))
            elif pos[i] == min:
                min_lines.append(chr(ord('A')+i))
            if pos[i] > max:
                max = pos[i]
                max_lines.clear()
                max_lines.append(chr(ord('A')+i))
            elif pos[i] == max:
                max_lines.append(chr(ord('A')+i))
        if first[0] == "":
            move_to(ma_ligne*compte+1,0)
            erase_line()
            en_couleur(CL_GREEN)
            if len(max_lines) > 1:
                print('Sont en tête '," ".join(max_lines),': ' , max)
            elif len(max_lines) == 1:
                print('La première poule est ' if poule else "Le premier cheval est ",max_lines[0],': ' , max)
            move_to(ma_ligne*compte+2,0)
            erase_line()
            en_couleur(CL_GREEN)
            if len(min_lines) > 1:
                print('Sont à la traine '," ".join(min_lines),': ' , min)
            elif len(min_lines) == 1:
                print('La dernière poule est ' if poule else "Le dernier cheval est ",min_lines[0],': ' , min)
            move_to(ma_ligne*compte+3,0)
            erase_line()
            en_couleur(CL_LIGHTBLU)
            print("Votre pari: " + pari)
        else:
            move_to(ma_ligne*compte+1,0)
            erase_line()
            en_couleur(CL_YELLOW)
            print('Victoire de ',first,'!!! Le classement est ', "-".join(first))
            move_to(ma_ligne*compte+2,0)
            erase_line()
            print("Bravo ! Vous avez gagné !" if pari == first else "Oupss perdu")
            move_to(ma_ligne*compte+3,0)
            erase_line()
        lock.release()
        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1,5))
        finally :
            pass

#------------------------------------------------
def prise_en_compte_signaux(signum, frame) :
    # On vient ici en cas de CTRL-C p. ex.
    move_to(Nb_process+11, 1)
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")

    for i in range(Nb_process):
        mes_process[i].terminate()
    # bande_son_process.terminate()
    move_to(Nb_process*compte+1, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)
# ---------------------------------------------------
# La partie principale :
if __name__ == "__main__" :
    poule = False
    compte = 5 if poule else 3
    Nb_process=4
    temp = []
    for i in range(Nb_process):
        temp.append(chr(ord('A')+i))
    parier = False
    while not parier:
        print("Participent: "+" ".join(temp))
        pari = input('Sur quel cheval pariez vous ? ')
        if pari.upper() in temp:
            parier = True
        else:
            effacer_ecran()
            print("Ce cheval ne participe pas !")
    # Une liste de couleurs e affecter aleatoirement aux chevaux
    lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
                CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]

    LONGEUR_COURSE = 130 # Tout le monde aura la même copie (donc no need to have a 'value')

    keep_running=mp.Value(ctypes.c_bool, True)
    first= mp.Array(ctypes.c_wchar_p, [""]*Nb_process)
    pos= mp.Array(ctypes.c_int, [0]*Nb_process)
    mes_process = [0 for i in range(Nb_process+1)]

    # signal.signal(signal.SIGINT , prise_en_compte_signaux)
    # signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()
    lock = mp.Lock()
    for i in range(Nb_process):  # Créé Nb_process  processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i, keep_running, pos, first, lock, LONGEUR_COURSE, poule,
                                                             compte, lyst_colors))
    mes_process[Nb_process] = mp.Process(target=arbitre, args= (Nb_process+6, keep_running, pos, first, pari, lock,
                                                                LONGEUR_COURSE, poule))

    move_to(Nb_process*compte+10, 1)
    print("tous lances, Controle-C pour tout arrêter")

    for i in range(Nb_process+1):  # Lancer Nb_process  processus
         mes_process[i].start()
    # On attend la fin de la course
    for i in range(Nb_process): mes_process[i].join()
    mes_process[Nb_process].join()
    move_to(Nb_process*compte+12, 1)
    curseur_visible()
    # bande_son_process.terminate()
    print("Fini")
