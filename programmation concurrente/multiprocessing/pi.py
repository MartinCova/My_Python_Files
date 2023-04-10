# Martin COVA et Hugues FARTHOUAT

import random, time, ctypes
import multiprocessing as mp
 
# calculer le nbr de hits dans un cercle unitaire (utilisé par les différentes méthodes)
def frequence_de_hits_pour_n_essais(nb_iteration,nb_hits):
    count = 0
    for i in range(nb_iteration):
        x = random.random()
        y = random.random()
        # si le point est dans l’unit circle
        if x * x + y * y <= 1:
            count += 1
    nb_hits.value += count

if __name__ == "__main__":
    # Nombre d’essai pour l’estimation
    nb_total_iteration = 10000000
    nb_hits=mp.Value(ctypes.c_int, True)
    nano_time_start = time.time()*1000.0
    frequence_de_hits_pour_n_essais(nb_total_iteration,nb_hits)
    nano_time_end = time.time()*1000.0
    print("Valeur estimée Pi par la méthode Mono−Processus : ", 4 * nb_hits.value / nb_total_iteration)
    print("En " + str(nano_time_end-nano_time_start) + " ms")
    nb_hits.value = 0
    #Nombre de process
    k = 10
    mes_process = [0 for i in range(k+1)]
    nano_time_start = time.time()*1000.0
    for i in range(k):  # Créé Nb_process  processus
        mes_process[i] = mp.Process(target=frequence_de_hits_pour_n_essais, args= (int(nb_total_iteration/k),nb_hits))
        mes_process[i].start()
    for i in range(k): mes_process[i].join()
    nano_time_end = time.time()*1000.0
    print("Valeur estimée Pi avec ",k," process : ", 4 * nb_hits.value / nb_total_iteration)
    print("En " + str(nano_time_end-nano_time_start) + " ms")
    #TRACE :
    # Calcul Mono−Processus : Valeur estimée Pi par la méthode Mono−Processus : 3.1412604