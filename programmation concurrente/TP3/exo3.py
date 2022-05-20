import os
import sys
from random import randint


(nbpair,nbpairw) = os.pipe()
(nbimpair,nbimpairw) = os.pipe()
(sommepair,sommepairw) = os.pipe()
(sommeimpair,sommeimpairw) = os.pipe()


def generator(N):
    os.close(nbpair)
    os.close(nbimpair)
    os.close(sommepairw)
    os.close(sommeimpairw)
    for i in range(0, N):
        a = randint(0, 5)
        print(a)
        if a % 2 == 0:
            a_bytes = a.to_bytes(4, byteorder="little", signed=True)
            os.write(nbpairw, a_bytes)
        else:
            a_bytes = a.to_bytes(4, byteorder="little", signed=True)
            os.write(nbimpairw, a_bytes)
    fin = -1
    os.write(nbpairw, fin.to_bytes(4, byteorder="little", signed=True))
    os.write(nbimpairw, fin.to_bytes(4, byteorder="little", signed=True))

    somme_pair_bytes = os.read(sommepair, 4)
    somme_pair = int.from_bytes(somme_pair_bytes, byteorder="little", signed=True)
    somme_impair_bytes = os.read(sommeimpair, 4)
    somme_impair = int.from_bytes(somme_impair_bytes, byteorder="little", signed=True)
    somme = somme_pair + somme_impair
    print("somme totale :", somme)



def filtre_pair():
    os.close(nbpairw)
    os.close(nbimpairw)
    os.close(sommepair)
    os.close(sommeimpair)
    somme_pair = 0
    a_bytes = os.read(nbpair, 4)
    a = int.from_bytes(a_bytes,byteorder="little", signed=True)
    while a != -1:
        somme_pair += a
        a_bytes = os.read(nbpair, 4)
        a = int.from_bytes(a_bytes, byteorder="little", signed=True)
    os.write(sommepairw, somme_pair.to_bytes(4, byteorder="little", signed=True))
    print("somme_pair :", somme_pair)


def filtre_impair():
    os.close(nbpairw)
    os.close(nbimpairw)
    os.close(sommepair)
    os.close(sommeimpair)
    somme_impair = 0
    a_bytes = os.read(nbimpair, 4)
    a = int.from_bytes(a_bytes, byteorder="little", signed=True)
    while a != -1:
        somme_impair += a
        a_bytes = os.read(nbimpair, 4)
        a = int.from_bytes(a_bytes, byteorder="little", signed=True)
    os.write(sommeimpairw, somme_impair.to_bytes(4, byteorder="little", signed=True))
    print("somme_impair :", somme_impair)


if os.fork() == 0:
    generator(10)
    sys.exit(0)

if os.fork() == 0:
    filtre_impair()
    sys.exit(0)

filtre_pair()
