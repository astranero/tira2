
from random import randint
import time


class Union_find:
    def __init__(self, n):
        self.maara = n
        self.vanhempi = list(range(0, self.maara+1))
        self.koko = [1]*(self.maara+1)
        self.count()

    def find(self,a):
        while self.vanhempi[a] != a:
            a=self.vanhempi[a]
        return a
    
    def unify(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.koko[a] < self.koko[b]:
                a,b=b,a
            self.koko[a] += self.koko[b]
            self.vanhempi[b] = a
    
    def count(self):
        alku = time.time()
        n=1
        while n <= self.maara:
            a = randint(1, self.maara)
            b = randint(1, self.maara)
            self.unify(a,b)
            n+=1
        loppu = time.time()
        print(len(set(self.vanhempi))-1)
        print(loppu-alku)

if __name__ == "__main__":
    Union_find(100)
    Union_find(1000)
    Union_find(10000)
    Union_find(100000)