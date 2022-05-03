from heapq import heapify, heappop, heappush
from queue import PriorityQueue
from random import choice

class NewRoads:
    def __init__(self,n):
        self.pituus = n
        self.verkko = {}
        for i in range(1,self.pituus+1): self.verkko[i] = []
        self.hinta = {}
       

    def add_road(self,a,b,x):
        self.verkko[a].append((a,b))
        self.verkko[b].append((b,a))
        if (a,b) in self.hinta: 
            if self.hinta[(a,b)] > x:
                self.hinta[(a,b)] = x
        else: self.hinta[(a,b)] = x
        if (b,a) in self.hinta: 
            if self.hinta[(b,a)] > x:
                self.hinta[(b,a)] = x
        else: self.hinta[(b,a)] = x
     

    def prim(self):
        
        pq = []
        mukana = {}
        for solmu in self.verkko:
            mukana[solmu] = False
        mukana[1] = True
        for kaari in self.verkko[1]:
            heappush(pq, (self.hinta[kaari], kaari))
        
        joukko = []
        while pq:
            hinta, kaari = heappop(pq)
            if mukana[kaari[1]]: continue
            mukana[kaari[1]] = True
            joukko.append((kaari))
            for kaari in self.verkko[kaari[1]]:
                heappush(pq,(self.hinta[kaari], kaari))
        return joukko
    
    def min_cost(self):
        joukko = self.prim()
        if len(joukko) < self.pituus-1:
            return -1

        hinta = 0
        for kaari in joukko:
            hinta += self.hinta[kaari]
        return hinta

if __name__ == "__main__":
    n = NewRoads(5)
    print(n.min_cost())
    n.add_road(4,5,8)
    print(n.min_cost())
    n.add_road(3,5,1)
    n.add_road(4,5,2)
    n.add_road(1,2,10)
    print(n.min_cost())
    n.add_road(2,4,5)
    n.add_road(3,5,4)
    print(n.min_cost())