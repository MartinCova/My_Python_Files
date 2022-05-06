import os
import sys

"exo2"
"""for i in range(3):
    pid = os.fork()
    print("i: ", i, " je suis le processus : ", os.getpid(), "mon pere est : ", os.getppid(), "retour: ", pid)"""


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

"Exercice 5"


