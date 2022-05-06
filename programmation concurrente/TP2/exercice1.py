import os
import sys

N = 10
i = 1

while i < N:
    i += 1
    print(i)
if i == N:
    os.execlp("python", "python", "test.py")
