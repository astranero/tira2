
def count(n):
    valimuisti = {}
    return tornit(valimuisti, n)

def tornit(valimuisti, n):
    if n in valimuisti: return valimuisti[n]
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    arvot = tornit(valimuisti, n-1) + tornit(valimuisti, n-2) + tornit(valimuisti, n-3)
    valimuisti[n] = arvot
    return arvot

if __name__ == "__main__":
    print(count(50))