import time

def abc(r):
    return r*9/5 + 32

t0 = time.clock()
abc(100000)
t1 = time.clock() - t0
print(" t = ", t1)