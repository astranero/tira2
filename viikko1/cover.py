def count(n, m, k):
    matriisi = [[0]*m for i in range(n)]
    etsi(matriisi, 0, 0, n ,m , k)

def etsi(matriisi, x, y, n, m, k):
    if k < 0:
        print(matriisi) 
        return
    for i in range(x, n):
        for j in range(y, m):
            matriisi[i][j] = 1
            etsi(matriisi, x-1, y+1, n, m, k-1)
            matriisi[i][j] = 0


if __name__ == "__main__":
    print(count(2,2,4)) # 8
    #print(count(2,3,3)) # 13
    #print(count(4,4,1)) # 1
    #print(count(4,3,10)) # 3146
    #print(count(4,4,16)) # 70878