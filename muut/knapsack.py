
def count(t):
    w = [0] + t
    W = [False]*sum(w)
    W[0] = True
    knapsack(len(w)-1, w, W)
    
    pituus = 0
    for i in range(len(W)):
        if W[i] == True: 
            pituus +=1
    return pituus-1

def knapsack(k, w, W):
    if W[k]:
        W[w[k]] = True
        return 0

    indeksi = knapsack(k-1, w, W)
    for j in range(indeksi, -1,-1):
        if W[j] and (j+w[k] <= sum(w)):
            W[j+w[k]] = True
            indeksi = j + w[k]
    W[w[k]] = True
    return indeksi

if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    #print(count([2,2,2,3,3,3])) # 13
    #print(count([42,5,5,100,1,3,3,7])) # 91