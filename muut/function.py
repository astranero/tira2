def f(lista, n):
    if lista[n] != 0: 
        return lista[n]
    if n <= 2:
        return n
    arvo = f(lista, n-1) + f(lista, n-2) + f(lista, n-3)
    lista[n] = arvo
    return arvo

if __name__ == "__main__":
    lista = []
    for i in range(310):
        lista.append(0)
    print(f(lista, 300))