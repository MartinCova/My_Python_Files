import os, sys

(dfr, dfw) = os.pipe()
(dfr2, dfw2) = os.pipe()
pid = os.fork()


def lirefichier(path):
    if pid != 0:
        os.close(dfr)
        os.dup2(dfw, 1)
        os.close(dfw)
        os.execlp("cat", "cat", path)
    else:
        os.close(dfw)
        os.dup2(dfr, 0)
        os.close(dfr)
        os.execlp("wc", "wc", "-l")
    sys.exit(0)


def trifichier(path):
    if pid != 0:
        os.close(dfr)
        os.dup2(dfw, 1)
        os.close(dfw)
        os.close(dfr2)
        os.close(dfw2)
        os.execlp("sort", "sort", path)

    else:
        pid2 = os.fork()
        if pid2 != 0:
            os.close(dfw)
            os.dup2(dfw2, 1)
            os.dup2(dfr, 0)
            os.close(dfr)
            os.close(dfr2)
            os.close(dfw2)
            os.execlp("grep", "grep", "os")
        else:
            os.close(dfw2)
            os.dup2(dfr2, 0)
            os.close(dfr2)
            os.close(dfr)
            os.close(dfw)
            os.execlp("tail", "tail", "-n", "2")
    sys.exit(0)

#lirefichier('exo1.py')

trifichier('exo1.py')

