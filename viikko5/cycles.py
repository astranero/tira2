class Cycles:
    def __init__(self,n):
        self.solmu_maara = n
        self.vieruslista = {}
        self.solmuja_lisatty = False
        for i in range(1,self.solmu_maara+1):
            self.vieruslista[i] = []

    def add_edge(self,a,b):
        self.vieruslista[a].append(b)
        self.solmuja_lisatty = True

    def check(self):
      
        self.loytyi_sykli = False

        visited = ["Valkoinen" for i in range(0,self.solmu_maara+1)]
        for solmu in self.vieruslista:
            if visited[solmu] == "Valkoinen":
                self.search(solmu, visited)
        return self.loytyi_sykli

    def search(self, solmu, visited): 
        visited[solmu] = "Harmaa"        
    
        for naapuri in self.vieruslista[solmu]:
            if visited[naapuri] == "Harmaa":
                self.loytyi_sykli = True
                return 
            elif visited[naapuri] == "Valkoinen":
                self.search(naapuri, visited)

        visited[solmu] = "Musta"
        return False

if __name__ == "__main__":
    c = Cycles(5)
    print(c.check())
    c.add_edge(5,5)
    print(c.check())
    c.add_edge(3,4)
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(1,3)
    c.add_edge(4,2)
    print(c.check())
