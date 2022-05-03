import math

class BestRoute:
    def __init__(self,n):
        self.maara = n
        self.vieruslista = {}

    def add_road(self,a,b,x):
        if (a,b) in self.vieruslista:
            arvo = min(self.vieruslista[(a,b)], x)
        else: arvo = x
        self.vieruslista[(a,b)] = arvo
        self.vieruslista[(b,a)] = arvo
        
    def find_route(self,a,b):
        
        etaisyys = {}
        for kaari in self.vieruslista:
            (alku, loppu) = kaari
            etaisyys[alku] = math.inf
            etaisyys[loppu] = math.inf
        etaisyys[a] = 0
        
        while True:
            muutos = False
            for kaari in self.vieruslista:
                (alku,loppu) = kaari
                nykyinen = etaisyys[loppu]
                uusi = etaisyys[alku] + self.vieruslista[kaari]
                if uusi < nykyinen:
                    etaisyys[loppu] = uusi
                    muutos = True
            if not muutos: break
            
       
        if b in etaisyys:
            if etaisyys[b] != math.inf: 
              return etaisyys[b]
        return -1

if __name__ == "__main__":
    b = BestRoute(5)
    b.add_road(4,5,4)
    print(b.find_route(3,4))
    b.add_road(4,5,9)
    print(b.find_route(3,5))
    print(b.find_route(1,5))
    b.add_road(1,4,5)
    print(b.find_route(1,4))
    b.add_road(3,4,7)
    b.add_road(2,3,1)
    print(b.find_route(2,5))