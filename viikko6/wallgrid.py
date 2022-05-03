class WallGrid:
    def __init__(self,n):
        self.n = n
        self.kaarilista = []
        self.vanhempi = {}
        self.koko = {}
        for i in range(1, self.n+1): 
            self.vanhempi[i] = i
            self.koko[i] = 0

    def find(self, x):
        while self.vanhempi[x] != x:
            x = self.vanhempi[x]
        return x

    def union(self, x,y):
        a = self.find(x)
        b = self.find(y)
        if self.koko[a] < self.koko[b]: a,b = b,a
        self.vanhempi[b] = a
        self.koko[a] += 1

    def remove(self,x,y):
        self.kaarilista.append((x,y))

    def count(self):
        pass

if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2,2)
    w.remove(4,2)
    print(w.count()) # 2
    w.remove(3,2)
    print(w.count()) # 1
    w.remove(2,4)
    w.remove(2,4)
    w.remove(4,4)
    print(w.count()) # 3
    w.remove(3,3)
    print(w.count()) # 3
    w.remove(3,4)
    print(w.count()) # 1