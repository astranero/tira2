def count(n):
    valmiit = []
    lista = []
    number(n, valmiit, lista)
    return len(valmiit)
 
def number(n, valmiit, lista, indeksi=0):
    if n < 0: return
    if n == 0:
        valmiit.append((lista[:]))
        return True
 
    if indeksi == 0: viimeksi = 1
    else: viimeksi = lista[indeksi-1]
    
    for i in range(viimeksi,n+1):    
            lista.append(i)
            number(n-i, valmiit, lista, indeksi+1)
            lista.pop()
    
    
 
if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174
