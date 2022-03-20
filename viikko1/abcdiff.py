import abc


def create(n):
    arvot = []
    return abcdiff(n, arvot)

def abcdiff(n,arvot, s="",valikko="ABC"):
    if n == 0: 
        arvot.append(s)
        return 

    for i in range(0,3):
        if tarkistus(s,valikko[i]):
            abcdiff(n-1, arvot, s+valikko[i])
    return arvot

def tarkistus(s, valinta):
    if s == "": return True
    if s[-1] != valinta: return True
    return False

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 43