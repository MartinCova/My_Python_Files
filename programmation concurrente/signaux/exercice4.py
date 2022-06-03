import os
import signal
import sys
import time

pidfils =0
# exercice 4
pid = os.fork()
if pid != 0:
    for i in range(3):
        try :
            time.sleep(1)
        except : pass
        print("je suis le père")
        print(i)
        if i == 2:
            os.kill(pidfils,signal.SIGKILL)
else:
    pidfils = os.getpid()
    while True:
        try:
            time.sleep(1)
        except: pass
        print("je suis le fils")
