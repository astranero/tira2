def count(n):
    if n == 0: return 0
    lista = []
    for i in range(n+1):
        lista.append(0)
    return jump(lista, n)

def jump(lista, n, vastaus=0):
    if n < 0: return 0
    if lista[n] != 0: 
        return lista[n]
    if n == 0:
        return 1

    for i in range(1,6+1):
        vastaus += jump(lista, n-i)
        lista[n] = vastaus
    return vastaus

if __name__ == "__main__":
    print(count(996))