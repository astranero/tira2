def create(s):
    anagrammi_lista = []
    anagramm(s, anagrammi_lista)
    return sorted(anagrammi_lista)

def anagramm(valikko, anagrammi_lista, merkkijono=""):
    if valikko == "":
        if merkkijono not in anagrammi_lista:
            anagrammi_lista.append(merkkijono)
        return

    for i in range(0,len(valikko)):
        alku = valikko[0:i]
        loppu = valikko[i+1:len(valikko)]
        anagramm(alku + loppu, anagrammi_lista, merkkijono+valikko[i])
    return 

if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260