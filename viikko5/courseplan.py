class CoursePlan:
    def __init__(self):
        self.vieruslista = {}

    def add_course(self,course):
        self.vieruslista[course] = []

    def add_requisite(self,course1,course2):
        self.vieruslista[course1].append(course2)

    def find(self):
        visited = {}
        self.kurssit = []
        self.loytyi_sykli = False
        for kurssi in self.vieruslista:
            visited[kurssi] = "valkoinen"
        
        for kurssi in self.vieruslista:
            if visited[kurssi] == "valkoinen":
                self.dfs_search(kurssi, visited)
        self.kurssit.reverse()

        if not self.loytyi_sykli: return self.kurssit
        else: return None

    def dfs_search(self, solmu, visited):
        visited[solmu] = "harmaa"
            
        for kurssi in self.vieruslista[solmu]:
            if visited[kurssi] == "valkoinen":
                self.dfs_search(kurssi, visited)
            elif visited[kurssi] == "harmaa":
                self.loytyi_sykli = True
                return

        self.kurssit.append(solmu)
        visited[solmu] = "musta"        

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None