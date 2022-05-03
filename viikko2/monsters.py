
def count(r):
    if r[0][0] == "#":
        return -1
    n = len(r)+1

    taulu = [[0]*(n) for i in range((n))]
    for i in range(0, n-1):
        for j in range(0, n-1):
            if r[i][j] == "#":
                taulu[i+1][j+1] = "#"
            elif r[i][j] == "@":
                taulu[i+1][j+1] = "@"

    
    for y in range(1, n):
        for x in range(1, n):
            
            if taulu[y][x]== "@":
                taulu[y][x] = 1
            if taulu[y][x] =="#":
                continue
            if y-1 != 0 and x-1 != 0:
                if taulu[y][x] != "#":
                    tmp1, tmp2 = taulu[y][x-1], taulu[y-1][x]
                    if tmp1 == "#" and tmp2 != "#":
                        taulu[y][x] += tmp2
                    elif tmp2 == "#" and tmp1 != "#":
                        taulu[y][x] += tmp1
                    elif tmp1 != "#" and tmp2 != "#":
                        taulu[y][x] += min(tmp1, tmp2)
                    else: taulu[y][x] = "#"
            
            elif y-1 == 0 and x-1 != 0:
                if taulu[y][x] != "#"  and taulu[y][x-1] != "#":
                        taulu[y][x] += taulu[y][x-1]
                else: taulu[y][x] = "#"
            elif y-1 != 0 and x-1 == 0:
                if taulu[y][x] != "#" and taulu[y-1][x] != "#":
                    taulu[y][x] += taulu[y-1][x]
                else: taulu[y][x] = "#"
                    
   
    if taulu[len(taulu)-1][len(taulu)-1] != "#":
        return taulu[len(taulu)-1][len(taulu)-1]
    else: return -1

def kuva(r):
    for i in range(len(r)):
        print(r[i])

if __name__ == "__main__":
    r = ["...@.",
         ".....",
         "..#..",
         "..@..",
         "@...@"]
    print(count(r)) # 1

    r= ["@..@#",
        ".@@@@",
        "@.@#@",
        "..#..",
        "@@.@."]
    print(count(r))

    r = ["#@.@#",
         "@...@",
         "@@@##",
         "@#@@@",
         "@.#@@"]
    print(count(r))

    r = ["@@@#@",
         ".#@#@",
         ".@#@#",
         "##.@@",
         "#@.@@"]
    print(count(r))

    r = [".##@.",
         "..@#.",
         "###@#",
         "..#.@",
         "#@@.."]
    print(count(r))