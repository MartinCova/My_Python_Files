import multiprocessing as mp
import os, time,math, random, sys, ctypes, signal


def startProcess(id,sem,lock,billes,billes_need):
    m = 4
    for i in range(m):
        print("Process:",id,"m =",i)
        demander(id,sem,lock,billes,billes_need)
        work(id,sem,billes,billes_need)
        rendre(id,sem,lock,billes,billes_need)


def demander(id,sem,lock,billes,billes_need):
    sem.acquire()
    print("Process:",id,"demander")
    while lock.acquire() and billes.value < billes_need:
        lock.release()
    billes.value -= billes_need
    lock.release()
    sem.release()


def work(id,sem,billes,billes_need):
    print("Process:",id,"sleep")
    time.sleep(1)


def rendre(id,sem,lock,billes,billes_need):
    lock.acquire()
    billes.value += billes_need
    print("Process:",id,"rendre", "=> Billes disponibles: ",billes.value)
    lock.release()


def controlleur(sem,lock,billes,max_billes):
    while 1:
        if lock.acquire() and 0 <= billes.value <= max_billes:
            lock.release()
            time.sleep(1)
            print("Billes disponibles:",billes.value)
        else:
            print("/!\\C/!\\", "Erreur dans le compte des billes")
            sem.acquire()


# La partie principale :
if __name__ == "__main__" :
    Nb_process = 4
    mes_process = [0 for i in range(Nb_process)]
    billes = mp.Value(ctypes.c_int, True)
    billes.value = 12
    lockPrincipale = mp.Lock()
    lock = mp.Lock()
    for i in range(Nb_process):  # Créé Nb_process  processus
        mes_process[i] = mp.Process(target=startProcess, args=(i, lockPrincipale, lock, billes, 4))
        mes_process[i].start()
    controlleur = mp.Process(target=controlleur, args=(lockPrincipale, lock, billes, billes.value))
    controlleur.start()
    for i in range(Nb_process): mes_process[i].join()
    controlleur.terminate()
    print("fin")
