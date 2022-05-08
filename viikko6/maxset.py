class MaxSet:
    def __init__(self,n):
        self.maara = n
        self.vanhempi = list(range(0, self.maara+1))
        self.size = [1]*(self.maara+1)
        self.suurin = 1
        
    def find(self,arvo):
        arvo = arvo
        while self.vanhempi[arvo] != arvo:
            arvo = self.vanhempi[arvo]
        return arvo

    def merge(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a,b = b,a
            self.size[a] += self.size[b]
            self.vanhempi[b] = a
        if self.size[a] > self.suurin:
            self.suurin = self.size[a]

    def get_max(self):
        return self.suurin

if __name__ == "__main__":
    m = MaxSet(5)
    m.merge(4,5)
    m.merge(2,3)
    print(m.get_max())
    print(m.get_max())
    m.merge(4,5)
    m.merge(4,3)
    m.merge(2,5)
    m.merge(4,5)
    print(m.get_max())
    m.merge(3,4)