def count(n,a,b):
    lista = []
    for i in range(n+1):
        lista.append(0)
    return jump(lista, n, a, b)

def jump(lista, n, a, b, vastaus=0):
    if n < 0: return 0
    if lista[n] != 0: 
        return lista[n]
    if n == 0:
        return 1

    vastaus += jump(lista, n-a, a, b) + jump(lista, n-b, a,b)
    lista[n] = vastaus
    return vastaus

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456