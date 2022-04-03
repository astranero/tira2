def tornit(k):
    torni_osajoukko = {}
    return palikka_tavat(torni_osajoukko, k)

def palikka_tavat(torni_osajoukko, max, result=0):
    if max < 0: return 0
    if max in torni_osajoukko: 
        return torni_osajoukko[max]
    if max == 0:
        return 1

    for i in range(1,4):
        result += palikka_tavat(torni_osajoukko, max-i)
        torni_osajoukko[max] = result   
    return result
        

if __name__ == "__main__":
    print(tornit(250))