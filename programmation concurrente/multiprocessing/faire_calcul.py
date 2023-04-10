import random, time
import os
import multiprocessing as mp


# Elements pour afficher les resultats proprement
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen


def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')


def effacer_ecran() : print(CLEARSCR,end='')

# --------------------------------------------------------


def fils_calculette(fil_demande,fil_resultat):
    while True:
        calcul = fil_demande.get()
        res = eval(calcul[0])
        fil_resultat.put([res,calcul[1]])
        time.sleep(2)


def demande_calcul(fil_demande,fil_resultat, id):
    while True:
        id_perso = id
        result = False
        # Le pere envoie au fils un calcul aléatoire à faire et récupère le résultat
        opd1 = random.randint(1, 10)
        opd2 = random.randint(1, 10)
        operateur = random.choice(['+', '-', '*', '/'])
        str_commande = str(opd1) + operateur + str(opd2)
        fil_demande.put([str_commande,id_perso])

        while result == False:
            res = fil_resultat.get()
            if res[1] == id_perso:
                move_to(0,0)
                effacer_ecran()
                print("Le père numero " + str(id_perso) + " va demander à faire : ", str_commande)
                move_to(2, 0)
                if type(res[0]) == float:
                    arr = round(res[0],2)
                    print("Le Pere numero " + str(res[1]) + " a recu ", arr)
                else:
                    print("Le Pere numero " + str(res[1]) + " a recu ", res[0])
                move_to(4, 0)
                print('-' * 60)
                result = True
            else:
                fil_resultat.put(res)


if __name__ == "__main__":
    # création des queues, une où sont stockées les demandes de calcul et l'autre les resultats
    fil_demande = mp.Queue()
    fil_resultat = mp.Queue()

    # création des process demande et calcul
    Nb_process_calcul: int = 5
    Nb_process_demande: int = 5
    mes_process_calcul = [0 for i in range(Nb_process_calcul)]
    mes_process_demande = [0 for i in range(Nb_process_calcul)]

    # on leur donne un id propre pour pouvoir renvoyer les calculs fait au bon process
    id: int = 1
    for i in range(Nb_process_calcul):  # Lancer     Nb_process  processus
        mes_process_calcul[i] = mp.Process(target=fils_calculette, args=(fil_demande, fil_resultat))
        mes_process_calcul[i].start()

    for i in range(Nb_process_demande):  # Lancer     Nb_process  processus
        mes_process_demande[i] = mp.Process(target=demande_calcul, args=(fil_demande, fil_resultat, id))
        id += 1
        mes_process_demande[i].start()

    for i in range(Nb_process_demande):  # pour finir propre
        mes_process_demande[i].join()

    for i in range(Nb_process_calcul):  # pour finir propre
        mes_process_calcul[i].join()