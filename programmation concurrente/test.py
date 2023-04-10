import os, sys, time

# k=0
# print(os.getpid())
# while k < 3 :
#     print('je suis le process ' + str(os.getpid()) + ' et mon pere est ' + str(os.getppid()) + ' pour k =' + str(k))
#     if os.fork() == 0 :
#         k += 1
#     else :
#         print(os.getpid())
#     k += 1
# time.sleep(5)
# sys.exit(0)

# k = 3
# print(os.getpid())
# for i in range(k):
#     pid = os.fork()
#     # print('process '+ str(os.getpid()) + ' mon pere est ' + str(os.getppid()) )
#     if i == 2:
#         if pid == 0:
#             pass
#             print('cmd')
#         else:
#             print('jencontiune')
#             pass


print("A")
if os.fork() != 0:
    print('B')
    if os.fork() != 0:
        print('C')
else:
    time.sleep(0.001)
    print("D")
sys.exit(0)