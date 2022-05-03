
class LongPath:
    def __init__(self,n):
        self.pituus = n
        self.vieruslista = {}
        for i in range(1,n+1):
            self.vieruslista[i] = []
        self.lisatty = False
        self.polut = {}

    def add_edge(self,a,b):
        if a > b:
            self.vieruslista[b].append(a)
        elif b >= a:
            self.vieruslista[a].append(b)
        self.lisatty = True
        
    def calculate(self):        
        visited = ["valkoinen" for i in range(0,self.pituus+1)]
        self.pituudet = {}
        
        if self.lisatty:
            for solmu in self.vieruslista:
                self.dfs_search(solmu, visited)
            arvot = self.pituudet.values()
            return max(arvot)
        else: return 0

    def dfs_search(self, solmu, visited, counter=0):
        visited[solmu] = "harmaa"
        if solmu not in self.pituudet: self.pituudet[solmu] = 0
        
        for naapuri in self.vieruslista[solmu]:
            if visited[naapuri] == "valkoinen":
                self.dfs_search(naapuri, visited, counter+1)
                uusi = self.pituudet[naapuri] + 1
                vanha = self.pituudet[solmu]
                if uusi > vanha:
                    self.pituudet[solmu] = uusi

            elif visited[naapuri] == "musta":
                uusi = self.pituudet[naapuri] + 1
                vanha = self.pituudet[solmu]
                if uusi > vanha:
                    self.pituudet[solmu] = uusi
        
        visited[solmu] = "musta"

if __name__ == "__main__":
    l = LongPath(5)
    print(l.calculate())
    l.add_edge(3,5)
    print(l.calculate())
    print(l.calculate())
    l.add_edge(3,4)
    print(l.calculate())
    l.add_edge(5,4)
    l.add_edge(1,2)
    l.add_edge(3,1)
    print(l.calculate())