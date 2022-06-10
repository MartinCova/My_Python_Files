
import random, time
import os
import multiprocessing as mp


def fils_calculette(fil_demande,fil_resultat):
    while True:
        print("bonjour du fils, num : ", os.getpid())
        calcul = fil_demande.get()
        #print("c'est ce qui est dans le pipe", calcul)
        res = eval(calcul[0])
        print("Dans le fils, le resultat est = ", res)
        print("le fils envoie ", res)
        fil_resultat.put([res,calcul[1]])
        time.sleep(1)

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
                print("Le père numero "+ str(id_perso) +" va demander à faire : ", str_commande)
                print("Le Pere numero " + str(res[1]) +" a recu ", res[0])
                print('-' * 60)
                result = True
            else:
                fil_resultat.put(res)


if __name__ == "__main__":
    fil_demande = mp.Queue()
    fil_resultat= mp.Queue()
    Nb_process_calcul = 5
    Nb_process_demande = 5
    mes_process_calcul = [0 for i in range(Nb_process_calcul)]
    mes_process_demande = [0 for i in range(Nb_process_calcul)]
    id = 1
    for i in range(Nb_process_calcul):  # Lancer     Nb_process  processus
        mes_process_calcul[i] = mp.Process(target=fils_calculette, args= (fil_demande,fil_resultat))
        mes_process_calcul[i].start()

    for i in range(Nb_process_demande):  # Lancer     Nb_process  processus

        mes_process_calcul[i] = mp.Process(target=demande_calcul, args= (fil_demande,fil_resultat,id))
        id += 1
        mes_process_calcul[i].start()

    for i in range(Nb_process_demande):  # Lancer     Nb_process  processus
        mes_process_calcul[i].join()
