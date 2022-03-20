def tasajako(luvut, loppusumma, erotus, m):
    if m==len(luvut):
        return erotus == 0
    if abs(erotus) > loppusumma[m]: return False 
    if tasajako(luvut, loppusumma, erotus+luvut[m], m+1):
            return True
    else:
        return tasajako(luvut, loppusumma, erotus-luvut[m], m+1)

from timeit import default_timer as timer
import random

if __name__ == "__main__":
    n = 30
    toistot = 40
    ylaraja = 99999999
    random.seed()
    for i in range(toistot):
        luvut = [random.randint(1, ylaraja) for i in range(n)]
        luvut.sort(reverse=True)
        loppusumma = []
        for i in range(0,len(luvut)):
            for j in range(i,len(luvut)):
                loppusumma.append(luvut[j])
        alku = timer()
        jako = tasajako(luvut, loppusumma, 0, 0)
        loppu = timer()
        print('{0:f} sekuntia, ratkaisu: {1}'.format(loppu-alku, jako))