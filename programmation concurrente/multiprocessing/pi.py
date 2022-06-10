import ctypes
import random, time
import multiprocessing as mp

# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)

def frequence_de_hits_pour_n_essais(nb_iteration,nb_hits):
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1: count += 1
    nb_hits.value += count




if __name__ == "__main__":

    # Nombre d’essai pour l’estimation
    nb_total_iteration = 10000000
    nb_proc = 4
    nb_hits =mp.Value(ctypes.c_int, True)

    mes_process = [0 for i in range(nb_proc)]
    debut = time.time()
    for i in range(nb_proc):
        mes_process[i] = mp.Process(target=frequence_de_hits_pour_n_essais, args=(int(nb_total_iteration/nb_proc),nb_hits))
        mes_process[i].start()


    for i in range(nb_proc):
        mes_process[i].join()

    #for i in range(nb_proc): mes_process[i].join()
    fin = time.time()
    print("Valeur estimée Pi par la méthode Mono−Processus : ", 4* nb_hits.value/ nb_total_iteration)
    duree = fin-debut
    print('durée du calcul: ', duree,"secondes")
    #TRACE :
    # Calcul Mono−Processus : Valeur estimée Pi par la méthode Mono−Processus : 3.1412604