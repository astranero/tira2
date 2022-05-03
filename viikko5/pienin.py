from cmath import inf


class Cycles:
    def __init__(self,n):
        self.solmu_maara = n
        self.vieruslista = {}
        for i in range(1,self.solmu_maara+1): self.vieruslista[i] = []

    def add_edge(self,a,b):
        self.vieruslista[a].append(b)

    def check(self):
        self.pienin = [0 for i in range(0, self.solmu_maara+1)]
        visited = ["Valkoinen" for i in range(0,self.solmu_maara+1)]
        for solmu in self.vieruslista:
            if visited[solmu] == "Valkoinen":
                self.search(solmu, visited)
        return self.pienin
        
    def search(self, solmu, visited): 
        visited[solmu] = "Harmaa"        
        self.pienin[solmu] = solmu

        for naapuri in self.vieruslista[solmu]:
            if visited[naapuri] == "Valkoinen":
                self.search(naapuri, visited)
                self.pienin[solmu] = min(self.pienin[solmu], self.pienin[naapuri])

            if visited[naapuri] == "Musta": 
                self.pienin[solmu] = min(self.pienin[solmu], self.pienin[naapuri])
                
        visited[solmu] = "Musta"

if __name__ == "__main__":
    c = Cycles(10)
    c.add_edge(4,6)
    c.add_edge(4,7)
    c.add_edge(4,3)
    c.add_edge(6,9)
    c.add_edge(7,6)
    c.add_edge(7,10)
    c.add_edge(3,10)
    c.add_edge(3,5)
    c.add_edge(2,6)
    c.add_edge(2,5)
    c.add_edge(2,1)
    c.add_edge(1,5)
    c.add_edge(6,5)
    c.add_edge(5,8)
    c.add_edge(5,9)
    c.add_edge(8,9)
    c.add_edge(3,7)
    c.add_edge(1,3)
    print(c.check()[4])
