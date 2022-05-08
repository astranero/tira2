
class Planets:
    def __init__(self,n):
        # TODO

    def add_teleport(self,a,b):
        # TODO

    def calculate(self):
        # TODO

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2