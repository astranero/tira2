def count(t):
    kohdeSumma = sum(t)
    kolikot = [0] + t
    arvotaulu = [True]+[False]*kohdeSumma
    k = len(kolikot)-1
   
    mahdollisetSummat(arvotaulu, k, kolikot, kohdeSumma)
    summa = -1
    for i in range(len(arvotaulu)):
        if arvotaulu[i] == True: summa += 1
    return summa
 
def mahdollisetSummat(arvotaulu, k, kolikot, kohdeSumma, summa=0):
    if summa > kohdeSumma: return
    if k==0: 
        arvotaulu[summa] = True
        return 
 
    mahdollisetSummat(arvotaulu, k-1, kolikot, kohdeSumma, summa)
    mahdollisetSummat(arvotaulu, k-1, kolikot, kohdeSumma, summa+kolikot[k])
    arvotaulu[summa] = True
    return 
 
if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91