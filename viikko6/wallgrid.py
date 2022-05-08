class WallGrid:
    def __init__(self,n):
        self.n = n
        self.kaarilista = []
        self.matrix = []
        for i in range(0,self.n+1): 
            self.matrix.append([0]*(self.n+1))
        
    def find(self, arvo):
        x=arvo
        while self.vanhempi[x] != x:
            self.vanhempi[x] = self.vanhempi[self.vanhempi[x]]
            x = self.vanhempi[x]
        return x

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if self.koko[a] < self.koko[b]: 
            a,b = b,a
        self.vanhempi[b] = a
        self.koko[a] += self.koko[b]

    def remove(self,x,y):
        if not self.matrix[x][y]:
            self.matrix[x][y] = True
            self.naapuri((x,y), x+1, y)
            self.naapuri((x,y), x, y+1)
            self.naapuri((x,y), x-1, y)
            self.naapuri((x,y), x, y-1)   

    def naapuri(self, alku, x,y):
        if self.matrix[x][y]: 
            self.kaarilista.append(((x,y), alku))
            self.kaarilista.append(((alku), (x,y)))
        
    def count(self):
        self.vanhempi = {}
        self.koko = {}
                    
        for i in range(0,self.n):
            for j in range(0,self.n):
                if self.matrix[i][j]:
                    self.vanhempi[(i,j)] = (i,j)
                    self.koko[(i,j)] = 1

        for kaari in sorted(set(self.kaarilista)):
            if self.find(kaari[0]) != self.find(kaari[1]):
                self.union(kaari[0], kaari[1])
       
        joukko = set()
        for avain in self.vanhempi:
            joukko.add(self.vanhempi[avain])
        maara = len(joukko)
        return maara

if __name__ == "__main__":
    w = WallGrid(6)
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(5,4)
    print(w.count())
    print(w.count())
    w.remove(5,4)
    w.remove(2,2)
    w.remove(5,2)
    w.remove(3,3)
    print(w.count())
    print(w.count())
    w.remove(5,3)
    w.remove(4,3)
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(2,3)
    w.remove(3,4)
    print(w.count())
    print(w.count())
    print(w.count())
    w.remove(4,3)
    print(w.count())
    print(w.count())
    w.remove(4,3)
    print(w.count())
    print(w.count())
