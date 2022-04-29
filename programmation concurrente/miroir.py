import sys 

#miroir 1
'''
lst = ''
print (sys.argv[1])
for i in sys.argv[1]:
    lst = str(i) + lst

print(lst)
'''

# miroir 2  

k = len(sys.argv)-1
if k == 0:
    print('aucun argument; veuillez ressayer')
else:
    for j in range(k):
        lst = ''
        for i in sys.argv[j+1]:
            lst = str(i) + lst
        print(lst)

