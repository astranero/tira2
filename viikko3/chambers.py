from operator import le


def count(r):
    korkeus, leveys = len(r), len(r[0])
    paikka_numero = [[None]*len(r[0]) for i in range(len(r))]
    graph = {}
    numero = 1
    for j in range(1,korkeus):
        for i in range(1,leveys):
            paikka_numero[j][i] = numero
            numero += 1

    for j in range(1, korkeus):
        for i in range(1,korkeus):
            if r[j][i] == ".":
                numero = paikka_numero[j][i]
                graph[numero] = []
                check_direction(r, graph, paikka_numero, numero, j+1, i)
                check_direction(r, graph, paikka_numero, numero, j-1, i)
                check_direction(r, graph, paikka_numero, numero, j, i+1)
                check_direction(r, graph, paikka_numero, numero, j, i-1)
 
    return count_components(graph)
    
def check_direction(r, graph, paikka_numero, numero, j,i):
    if r[j][i] == "#":
        return False
    if r[j][i] == ".":
        if paikka_numero[j][i] not in graph:
            graph[paikka_numero[j][i]] = []
        graph[numero].append(paikka_numero[j][i])

def count_components(graph):
    vierailtu = set()
    osat = 0
    for alkio in graph:
        if is_room(graph, vierailtu, alkio):
            osat += 1
    return osat

def is_room(graph, vierailtu, alkio):
    if alkio in vierailtu:
        return False
    vierailtu.add(alkio)
    
    for naapuri in graph[alkio]:
        is_room(graph, vierailtu, naapuri)
    return True

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3
