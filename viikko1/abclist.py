def create(n):
    arvot = []
    return abclist(n, arvot)

def abclist(n,arvot, s="",valikko="ABC"):
    if n == 0: 
        arvot.append(s)
        return 
    abclist(n-1, arvot, s+valikko[0])
    abclist(n-1, arvot, s+valikko[1])
    abclist(n-1, arvot, s+valikko[2])
    return arvot

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243