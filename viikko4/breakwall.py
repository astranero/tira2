import math

def count(r):

    pituus, leveys = len(r)-1, len(r[0])-1
    lopetus = 0
    seinat = {}

    for j in range(1, pituus):
        for i in range(1, leveys):
            seinat[(j,i)] = math.inf
            if r[j][i] == "A":
                seinat[(j,i)] = 0
            if r[j][i] == "B":
                lopetus=(j,i)
   
    while True:
        muutos = False
        for j in range(1, pituus):
            for i in range(1, leveys):
                solmu = (j,i)
                a = naapuri(r, seinat, j-1, i, solmu)
                b = naapuri(r, seinat, j+1, i, solmu)
                c = naapuri(r, seinat, j, i-1, solmu)
                d = naapuri(r, seinat, j, i+1, solmu)
                if (a or b or c or d): muutos = True
        if not muutos: break
    return seinat[lopetus]

def naapuri(r, seinat, j, i, solmu):
    if r[j][i] == "#": return
    if r[j][i] == "*": paino = 1
    else: paino = 0
    nyky = seinat[(j,i)]
    uusi = seinat[solmu] + paino
    if uusi < nyky:
        seinat[(j,i)] = uusi
        return True

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2