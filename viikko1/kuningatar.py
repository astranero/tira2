def haku(n, kohta):
    if n == 12:
        global laskuri
        laskuri += 1 
    else:
        for y in range(0,len(kohta)):
            if voi_sijoittaa(kohta,n,y):
                kohta[n] = y
                haku(n+1, kohta)

def voi_sijoittaa(kohta,y,x):
    for i in range(0, y):
        if kohta[i] == x: return False
        if abs(i-y) == abs(kohta[i]-x): return False
    return True

if __name__ == "__main__":
    laskuri = 0
    taulu = [-1]*12
    haku(0, taulu)
    print(laskuri)