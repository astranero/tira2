from operator import index


def count(s):    
    cache = {}
    return hajotus(s, cache)  

def hajotus(s, cache, indeksi=0):
    if s in cache:
        return cache[s]
    if len(s) == 0 or len(s) == 1:
        return 0
    set = ["11", "00"]
    if s in set:
        return 1
    if indeksi >= len(s)-1:
        return 0

    maarat = 0
    maarat += hajotus(s, cache, indeksi+1)
    if s[indeksi] == s[indeksi+1]:
        maarat += hajotus(s[0:indeksi]+s[indeksi+2:len(s)], cache, 0)
    cache[s] = maarat
    return maarat

if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925