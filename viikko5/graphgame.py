class GraphGame:
    def __init__(self,n):
        self.pituus = n
        self.vieruslista = {}
        for i in range(1,self.pituus+1): self.vieruslista[i] = []

    def add_link(self,a,b):
        self.vieruslista[a].append(b)

    def winning(self,x):
        visited = ["valkoinen" for i in range(0,self.pituus+1)]
        self.totuusarvo = {}
        
        self.dfs_search(x, visited)
        return self.totuusarvo[x]


    def dfs_search(self, solmu, visited):
        visited[solmu] = "harmaa"
        if solmu not in self.totuusarvo: self.totuusarvo[solmu] = False

        for naapuri in self.vieruslista[solmu]:
            if visited[naapuri] == "valkoinen":
                self.dfs_search(naapuri, visited)
                if not self.totuusarvo[naapuri]:
                    self.totuusarvo[solmu] = True
                    
            if visited[naapuri] == "musta":
                if not self.totuusarvo[naapuri]:
                    self.totuusarvo[solmu] = True

        visited[solmu] = "musta"

if __name__ == "__main__":
    g = GraphGame(10)
    g.add_link(5,4)
    g.add_link(7,5)
    g.add_link(5,6)
    g.add_link(7,4)
    g.add_link(9,7)
    g.add_link(1,4)
    g.add_link(8,4)
    g.add_link(6,4)
    g.add_link(2,4)
    g.add_link(10,8)
    g.add_link(10,1)
    g.add_link(3,9)
    g.add_link(3,6)
    g.add_link(7,5)
    g.add_link(7,4)
    print(g.winning(3))
    g.add_link(2,4)
    g.add_link(8,6)
    print(g.winning(2))
    print(g.winning(6))
    g.add_link(2,4)
    g.add_link(7,2)
    print(g.winning(1))
    print(g.winning(8))
    g.add_link(3,6)
    g.add_link(9,7)
    g.add_link(8,5)
    g.add_link(10,6)
    g.add_link(8,3)
    print(g.winning(10))