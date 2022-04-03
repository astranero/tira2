def count(t):
    kohdeSumma = sum(t)
    kolikot = [0] + t
    
    arvotaulu = [True]+[False]*kohdeSumma
    k = len(kolikot)-1
    
    for i in range(0,k+1):
        for j in range(len(arvotaulu)-1, -1,-1):
            if arvotaulu[j]:
                arvotaulu[j + kolikot[i]] = True
    
    summa = -1
    for i in range(len(arvotaulu)):
        if arvotaulu[i]: summa +=1
    return summa
   
    
 
if __name__ == "__main__":
    print(count([2, 3, 1])) #6
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91