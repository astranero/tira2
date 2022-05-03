from heapq import heappop

class SameWeight:
    def __init__(self,n):
        self.pituus = n
        self.kaarilista = []
        
    def make_set(self, x):
        self.vanhempi[x] = x
        self.koko[x] = 1

    def add_edge(self,a,b,x):
        self.kaarilista.append((x,a,b))

    def find(self, arvo):
        while self.vanhempi[arvo] != arvo:
            arvo = self.vanhempi[arvo]
        return arvo

    def unify(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.koko[a] < self.koko[b]: 
            a,b = b,a
        self.vanhempi[b] = a
        self.koko[a] += self.koko[b]
        

    def check(self):
        max_kaarilista = sorted(self.kaarilista, reverse=True)
        min_kaarilista = sorted(self.kaarilista)
        min_paino = self.weight(min_kaarilista)
        max_paino = self.weight(max_kaarilista)
        if min_paino == max_paino: return True
        else: return False

    def weight(self, kaarilista):
        self.vanhempi = {}
        self.koko = {}
        for i in range(1, self.pituus+1): self.make_set(i)
        paino = 0
        count = self.pituus
        for kaari in kaarilista:
            if self.find(kaari[1]) != self.find(kaari[2]): 
                self.unify(kaari[1],kaari[2])
                paino += kaari[0]
                count-=1
        return paino if count == 1 else -1

if __name__ == "__main__":
    s = SameWeight(5)
    s.add_edge(1,4,1)
    s.add_edge(4,5,1)
    print(s.check())
    s.add_edge(1,3,1)
    print(s.check())
    s.add_edge(3,5,1)
    print(s.check())
    print(s.check())