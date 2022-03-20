def tasajako(luvut, erotus, m):
    if m==len(luvut):
        return erotus == 0
    else:
        if tasajako(luvut, erotus+luvut[m], m+1):
            return True
        else:
            return tasajako(luvut, erotus-luvut[m], m+1)

from timeit import default_timer as timer
import random

if __name__ == "__main__":
    n = 23
    toistot = 20
    ylaraja = 99999999
    random.seed()
    for i in range(toistot):
        luvut = [random.randint(1, ylaraja) for i in range(n)]
        alku = timer()
        jako = tasajako(luvut, 0, 0)
        loppu = timer()
        print('{0:f} sekuntia, ratkaisu: {1}'.format(loppu-alku, jako))