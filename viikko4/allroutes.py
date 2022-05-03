import math
from pydoc import visiblename
class AllRoutes:
    def __init__(self,n):
        self.maara = n
        self.vierusmatriisi = [[math.inf]*self.maara for i in range(self.maara)]
        self.kaaripainot = {}

    def add_road(self,a,b,x):
        if (a-1,b-1) in self.kaaripainot:
            arvo = min(self.kaaripainot[(a-1,b-1)],x)
        else: arvo = x
        self.kaaripainot[(a-1, b-1)] = arvo
        self.kaaripainot[(b-1, a-1)] = arvo
        
    def get_table(self):
        for j in range(self.maara):
            self.find_route(j)
        return self.vierusmatriisi

    def find_route(self,a):

        etaisyys = self.vierusmatriisi[a]
        etaisyys[a] = 0
        print(etaisyys)
        while True:
            muutos = False
            for kaari in self.kaaripainot:
                (alku, loppu) = kaari
                nykyinen = etaisyys[loppu]
                uusi = etaisyys[alku] + self.kaaripainot[kaari]
                if uusi < nykyinen:
                    etaisyys[loppu] = uusi
                    muutos = True
            if not muutos: break
        
        for i in range(len(etaisyys)):
            if etaisyys[i] == math.inf:
                etaisyys[i] = -1


if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]