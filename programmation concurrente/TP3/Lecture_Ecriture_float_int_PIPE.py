# -*- coding: utf-8 -*-

'''
Transmettre un float via pipe en python
extrêment complexe du fait de choix de python
sur les variables à longueur dynamique
'''

import os

var = 12.5
piper,pipew = os.pipe()
#conversion de var en hexadecimal et encoder en byte pour être transmis sur un pipe
var_b = var.hex().encode()
#soucis on ne connais pas la longueur du tableau de byte en lecture du coup
#on crée un petit protocole d'échange
#| 4 octets | length octets |
#| length   | data          |
length = len(var_b)
#conversion de la taille en octet: 4 octet, little endian (architecture x86) peut être dans certain cas big endian
# signed=True si la valeur peut être négative
lb = length.to_bytes(4,byteorder="little",signed = True)
#écriture de la taille sur 4 octet
os.write(pipew,lb)
#ecriture des données
os.write(pipew,var_b)

#Lecture de la taille 4 octet
lb = os.read(piper,4)
#conversion inverse pour obtenir un entier "python", la taille (4) est déduite de la taille du contenu de lb
length = int.from_bytes(lb,byteorder="little",signed=True)
#lecture des données de longueur length
var_b = os.read(piper,length)
# conversion des données de bytes vers str (decode) puis conversion de str contenant de l'hexa vers float
var = float.fromhex(var_b.decode())
print(var)


'''
Soucis inexistant en C, par exemple, on écrit/lit le float directement avec write/read
sans avoir besoin de s'embêter

float var = 3.5;
write(pipew,&var,sizeof(var));
float var_read=0;
read(piper,&var_read,sizeof(var));
'''
