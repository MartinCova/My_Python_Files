import array
import multiprocessing as mp
import random
import time
import ctypes
import curses
import signal, sys


def client(liste_commande, lock, taille_tampon):
    nb_clients = 100
    menu = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
    while True:
        while len(liste_commande) < taille_tampon:
            lock.acquire()
            # choix au hasard du serveur
            commande = random.choice(menu)
            id_client = random.randint(1, nb_clients)
            liste_commande.append((id_client, commande))
            lock.release()
            time.sleep(random.randint(1, 2))


def serveur(id_perso_serveur, liste_commande, commande_perso_serveur, lock, commande_cuisine,commande_pret, occupe):
    reset = (0, ' ')
    while True:
        lock.acquire()
        if len(liste_commande) == 0:
            occupe[id_perso_serveur] = 0
            lock.release()
        else:
            try:
                commande_perso_serveur[id_perso_serveur] = liste_commande.pop(0)
                occupe[id_perso_serveur] = 1
                lock.release()
                # print(liste_commande)
                time.sleep(random.randint(4, 6))
                lock.acquire()
                commande_cuisine.append(
                    (commande_perso_serveur[id_perso_serveur][0], commande_perso_serveur[id_perso_serveur][1],
                     id_perso_serveur))
                lock.release()
                # print(commande_perso_serveur)
                # print(commande_cuisine)
                while commande_pret[0][2] != id_perso_serveur:
                    time.sleep(0.001)

                lock.acquire()
                # print('pret', commande_pret)
                lock.release()
                time.sleep(random.randint(1, 2))
                lock.acquire()
                commande_perso_serveur[id_perso_serveur] = reset
                lock.release()
            except IndexError:
                occupe[id_perso_serveur] = 0
                continue


def cuisto(id_perso_cuisto,lock, commande_cuisine, en_preparation, commande_pret):
    while True:
        lock.acquire()
        if len(commande_cuisine) == 0:
            lock.release()
        else:
            # print('dans la boucle')
            try:
                en_preparation[id_perso_cuisto] = commande_cuisine.pop(0)
                lock.release()
                # print('en prepa', en_preparation)
                time.sleep(random.randint(10, 20))
                lock.acquire()
                commande_pret[0] = en_preparation[id_perso_cuisto]
                en_preparation[id_perso_cuisto] = (0, ' ', 0)
                # print(commande_pret[0])
                lock.release()
            except IndexError:
                continue

        pass


def major(liste_commande, commande_perso_serveur, en_preparation, commande_pret, lock, commande_cuisine):
    # création de l'affichage
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    while True:
        lock.acquire()
        for i in range(len(commande_perso_serveur)):
            if commande_perso_serveur[i][0] == 0:
                stdscr.addstr(i, 0, 'le serveur ' + str(i+1) + ' ne traite pas de commande ')
                pass
            else:
                stdscr.addstr(i, 0, 'le serveur ' + str(i+1) + ' traite la commande ' + str(commande_perso_serveur[i]))
                pass
        stdscr.addstr(6, 0, 'les commandes clients en attente: ' + str(liste_commande))
        stdscr.addstr(7, 0, 'Nombre de commandes en attente: ' + str(len(liste_commande)))

        stdscr.addstr(8, 0, 'commande ' + str(commande_pret[0]) + ' servie au client')
        # stdscr.addstr(9, 0, str(commande_cuisine))
        # stdscr.addstr(5,0, str(len(en_preparation)))
        for i in range(len(en_preparation)):
            if en_preparation[i][0] == 0:
                stdscr.addstr(i+10, 0, 'le cuisinier ' + str(i + 1) + ' ne prepare pas de commande ')
                pass
            else:
                stdscr.addstr(i+10, 0,
                              'le cuisinier ' + str(i + 1) + ' prépare la commande ' + str(en_preparation[i]))
        lock.release()
        stdscr.refresh()

        # while True:
        #     lock.acquire()
        #     # print(commande_cuisine)
        #     print(en_preparation)
        #     lock.release()
        #     time.sleep(2)
    #
        # if stop_affi.value == True:
        #     # pour arreter le module:
        #     curses.nocbreak()
        #     stdscr.keypad(False)
        #     stdscr.clear()
        #     curses.echo()
        #     curses.endwin()
        #     pass


if __name__ == "__main__":
    # initialisation du verrou
    lock = mp.Lock()
    manager = mp.Manager()

    # initialisation du process client
    taille_tampon = 50
    lst_id_client = array.array('i', [0 for i in range(taille_tampon)])
    lst_menu_client = array.array('u', ['A' for i in range(taille_tampon)])
    liste_commande = manager.list()

    # initialisation des process serveurs
    nb_serveurs = 5
    mes_process_serveur = [0 for i in range(nb_serveurs)]
    commande_perso_serveur = manager.list([(0, ' ') for i in range(nb_serveurs)])
    id_perso_serveur = 0
    occupe = manager.list([0 for i in range(nb_serveurs)])

    # initialisation des process cuisto
    nb_cuisto = 2
    mes_process_cuisto = [0 for i in range(nb_cuisto)]
    en_preparation = manager.list([(0, ' ', 0), (0, ' ', 0)])
    id_perso_cuisto = 0
    commande_cuisine = manager.list([])
    commande_pret = manager.list([(0, ' ', 0)])

    for i in range(nb_serveurs):
        mes_process_serveur[i] = mp.Process(target=serveur, args=(id_perso_serveur, liste_commande,
                                                                  commande_perso_serveur, lock, commande_cuisine,
                                                                  commande_pret, occupe))
        mes_process_serveur[i].start()
        id_perso_serveur += 1

    process_client = mp.Process(target=client, args=(liste_commande, lock, taille_tampon))
    process_client.start()

    process_major = mp.Process(target=major, args=(liste_commande, commande_perso_serveur, en_preparation,
                                                   commande_pret, lock, commande_cuisine))
    process_major.start()

    for i in range(nb_cuisto):
        mes_process_cuisto[i] = mp.Process(target=cuisto, args=(id_perso_cuisto, lock, commande_cuisine,
                                                                en_preparation, commande_pret))
        mes_process_cuisto[i].start()
        id_perso_cuisto += 1

    process_client.join()
    process_major.join()

    for i in range(nb_serveurs):
        mes_process_serveur[i].join()

    for i in range(nb_cuisto):
        mes_process_cuisto[i].join()