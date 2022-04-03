from collections import deque

def count(r):
    korkeus, leveys = len(r), len(r[0])
    paikka_numero = [[None]*len(r[0]) for i in range(len(r))]
    graph = {}
    numero = 1
    alkusolmu = 0
    kohdesolmu = 0

    for j in range(1,korkeus):
        for i in range(1,leveys):
            paikka_numero[j][i] = numero
            if r[j][i] == "A":
                alkusolmu = numero
            if r[j][i] == "B":
                kohdesolmu = numero
            numero += 1

    for j in range(1, korkeus):
        for i in range(1,korkeus):
            if r[j][i] in (".", "A", "B"):
                numero = paikka_numero[j][i]
                graph[numero] = []
                check_direction(r, graph, paikka_numero, numero, j+1, i)
                check_direction(r, graph, paikka_numero, numero, j-1, i)
                check_direction(r, graph, paikka_numero, numero, j, i+1)
                check_direction(r, graph, paikka_numero, numero, j, i-1)

    vierailtu = set()
    return count_length(graph, alkusolmu, kohdesolmu, vierailtu)
    
       


def count_length(graph, alkusolmu, kohdesolmu, vierailtu):
    jono = deque()
    jono.appendleft((alkusolmu, 0))
    vierailtu.add(alkusolmu)
   
    while len(jono)>0:
        nykyinen, pituus = jono.pop()
        if nykyinen == kohdesolmu:
                return pituus
        
        for naapuri in graph[nykyinen]:
            if naapuri not in vierailtu:
                vierailtu.add(naapuri)
                jono.appendleft((naapuri, pituus+1))
    return -1

def check_direction(r, graph, paikka_numero, numero, j,i):
    if r[j][i] == "#":
        return False
    if r[j][i] in (".", "A", "B"):
        if paikka_numero[j][i] not in graph:
            graph[paikka_numero[j][i]] = []
        graph[numero].append(paikka_numero[j][i])

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7