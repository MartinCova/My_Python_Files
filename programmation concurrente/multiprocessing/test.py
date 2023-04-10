import os
import multiprocessing as mp
import sys
import signal
import time

x = 100
(dfr,dfw) = mp.Pipe()
if os.fork() == 0:
    y = 200
    dfw.send(y)
    time.sleep(2)
    sys.exit(0)
else:
    dfr.close()
    # (dfr, dfw) = mp.Pipe()
    x = dfr.recv()
    print("x=", x)
    sys.exit(0)


