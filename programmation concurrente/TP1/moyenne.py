import sys
import os
'''
k = len(sys.argv)-1
moyenne = 0 
if k == 0:
    print('aucun argument; veuillez ressayer')
else:
    for j in range(k):
        if float(sys.argv[j+1])>20 or float(sys.argv[j+1])<0:
            print('Notes non valides')
            break
        else:
            moyenne += float(sys.argv[j+1])
            
moyenne = moyenne/k
print(round(moyenne,2))
'''

N = 4
cas = 2
if cas == 1:
    for i in range(2,N+1):
        pid = os.fork()
        print(os.getpid())
        if pid == 0:
            print("processus fils")
        else:
            print("processus pere")
            break
    sys.exit(0)

elif cas == 2:
    for i in range(2,N+1):
        pid = os.fork()
        if pid == 0:
            print("je sui le processus fils ",os.getpid() ,'et mon processus père est' ,os.getppid())
            break
        else:
            print("processus pere")
            
    sys.exit(0)