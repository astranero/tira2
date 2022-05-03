class Cities:
    def __init__(self,n):
        self.kaupungit = {}
        for i in range(1,n+1):
            self.kaupungit[i] = []

    def add_road(self,a,b):
        self.kaupungit[a].append(b)
        self.kaupungit[b].append(a)

    def has_route(self,a,b):
        vierailtu = set()
        return self.find_route(a,b,vierailtu)

    def find_route(self, a, b, vierailtu):
        if a in vierailtu:
            return False
        vierailtu.add(a)
        
        if b in self.kaupungit[a]:
            return True    
       
        for naapuri in self.kaupungit[a]:
            if self.find_route(naapuri,b,vierailtu):
                return True
        return False
        
if __name__ == "__main__":
    c = Cities(5)
    c.add_road(2,3)
    c.add_road(1,2)
    print(c.has_route(3,4))
    c.add_road(2,5)
    print(c.has_route(4,5))
    c.add_road(1,3)
    c.add_road(3,4)
    print(c.has_route(2,3))
    print(c.has_route(3,5))
    print(c.has_route(3,4))