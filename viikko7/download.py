from heapq import heappush, heappop


class Download:
    def __init__(self,n):
        self.pituus = n
        self.vieruslista = {}
        self.kapasiteetti = {}
        for i in range(1,51):
            self.vieruslista[i] = []

    def add_link(self,a,b,x):
        self.vieruslista[a].append((b))
        self.vieruslista[b].append((a))
        if (a, b) in self.kapasiteetti:
            self.kapasiteetti[(a, b)]+=x
            self.kapasiteetti[(b, a)]=0
        else:
            self.kapasiteetti[(a, b)]=x
            self.kapasiteetti[(b, a)]=0

    def calculate(self,a,b):
        max_virtaus = 0
        self.vanhempi = [0]*(self.pituus+1)
        self.kap = self.kapasiteetti.copy()

        while self.bfs(a,b):
            min_kp = 99999

            x = b
            while x != a:
                min_kp = min(min_kp, self.kap[(self.vanhempi[x], x)])
                x = self.vanhempi[x]
            
            max_virtaus += min_kp

            v = b
            while v != a:
                self.kap[(self.vanhempi[v], v)] -= min_kp
                self.kap[(v, self.vanhempi[v])] += min_kp
                v = self.vanhempi[v]
        
        return max_virtaus

    def bfs(self,a,b):
        vierailtu = [False for i in range(0,self.pituus+1)]
        jono = []
        
        for naapuri in self.vieruslista[a]:
            paino = self.kap[(a,naapuri)]
            if paino > 0:
                heappush(jono, (paino,naapuri))
                self.vanhempi[naapuri] = a

        vierailtu[a] = True
        
        while jono:
            paino, solmu = heappop(jono)
            if not vierailtu[solmu]:
                vierailtu[solmu] = True

                for naapuri in self.vieruslista[solmu]:
                    paino = self.kap[solmu, naapuri]
                    if not vierailtu[naapuri] and paino > 0:
                        heappush(jono,(paino, naapuri))
                        self.vanhempi[naapuri] = solmu
        return vierailtu[b]

if __name__ == "__main__":
    d = Download(5)
    print(d.calculate(3,4))
    d.add_link(5,3,6)
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    print(d.calculate(5,1))
    d.add_link(5,4,9)
    d.add_link(1,2,10)
    print(d.calculate(3,1))
    print(d.calculate(2,4))
    print(d.calculate(5,4))
    d.add_link(5,2,9)
    print(d.calculate(1,5))
    d.add_link(3,5,2)
    d.add_link(1,3,2)
    d.add_link(5,4,9)
    print(d.calculate(5,4))
    print(d.calculate(2,3))
    print(d.calculate(1,3))
    print(d.calculate(3,2))
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    d.add_link(4,3,9)
    print(d.calculate(4,5))
    print(d.calculate(2,4))
    print(d.calculate(4,5))
    d.add_link(5,1,6)
    d.add_link(3,5,3)
    d.add_link(4,5,2)
    print(d.calculate(3,4))