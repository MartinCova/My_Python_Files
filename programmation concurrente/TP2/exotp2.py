import os
import sys
import time

"exo2"
"""for i in range(3):
    pid = os.fork()
    print("i: ", i, " je suis le processus : ", os.getpid(), "mon pere est : ", os.getppid(), "retour: ", pid)"""

"--------------------------------------------------------------"

"exo3"


"""def execommshell(commande):
    commandelst = commande.split(" ")
    print(commandelst)
    if len(commandelst) > 1 :
        os.execlp(commandelst[0], commandelst[0], commandelst[1])
    else:
        os.execlp(commandelst[0], commandelst[0])


commandeshell = ["ls -l", "who", "ps"]
process = 2
match process:
    case 1:
        for i in commandeshell:
            pid = os.fork()
            if pid == 0:
                print(pid)
                execommshell(i)
    case 2:
        for i in commandeshell:
            pid = os.fork()
            if pid == 0:
                execommshell(i)
            else:
                os.wait()"""


"--------------------------------------------------------"

"Exercice 4"
"""
n=0
for i in range(1,5):
    print(i)
    fils_pid = os.fork() #1
    if (fils_pid > 0) :
        os.wait() #3
        n = i*2
        break
print("n = ", n) #4
sys.exit(0)"""

"-------------------------------------------------------------"
"""
"Exercice 5"

def sousprog(i):
    print('je suis le processus : ', os.getpid(), 'et mon père est le : ', os.getppid())
    time.sleep(2*i)
    sys.exit(i)


'programme principal'
if len(sys.argv) - 1 == 1:
    N = sys.argv[1]
    for i in range(int(N)):
        pid = os.fork()
        if pid == 0:
            sousprog(i)
        else:
            os.wait()
else:
    print('c')
"""
"------------------------------------------------------------------"
"""
"Exercice 6"

import os, time, random, sys

for i in range(4):
    if os.fork() != 0:
        break
random.seed()
delai = random.randint(0, 4)
time.sleep(delai)
print("Mon nom est " + chr(ord('A')+i) + " j ai dormi " +
       str(delai) +  " secondes")
sys.exit(0)
"""

"-----------------------------------------"
"Exercice 7"

"""N = 2
for i in range(N):
    os.fork()
    os.fork()
print("Bonjour")
sys.exit(0)"""

