def count(r):
    esteet = [[(None, 999)]*len(r) for i in range(len(r))]
    maksimi_x, maksimi_y = len(r)-1, len(r)-1
    esteet[maksimi_y][maksimi_x]
    reitti(r, esteet, 0, 0, maksimi_y, maksimi_x)
   
    if esteet[maksimi_y][maksimi_x][0]:
        return esteet[maksimi_y][maksimi_x][1]
    else: return -1
   
def reitti(r, esteet, y, x, maksimi_y, maksimi_x, counter=0):
    if counter >= esteet[maksimi_y][maksimi_x][1]:
        return (False, counter)
        
    if y > maksimi_y or x > maksimi_x:
        return (False, counter)
    
    if r[y][x] == "#":
        esteet[y][x] = (False, counter)
        return (False, counter)
    
    if r[y][x] == "@":
        counter += 1
        
    if y == maksimi_y and x == maksimi_x:
        if counter < esteet[y][x][1]:
            esteet[y][x] = (True, counter)
        return (True, counter)
 
    tmp1 = reitti(r, esteet, y+1, x, maksimi_y, maksimi_x, counter)
    tmp2 = reitti(r, esteet, y, x+1, maksimi_y, maksimi_x, counter)
    totuusarvo1 = tmp1[0]
    totuusarvo2 = tmp2[0]
    counter1 = tmp1[1]
    counter2 = tmp2[1]

    if (totuusarvo1 or totuusarvo2) == False:
        esteet[y][x] = (False, counter1)
        return (False, counter1)
    elif totuusarvo1 == True and totuusarvo2 == False:
        esteet[y][x] = (totuusarvo1, counter)
        return (totuusarvo1, counter1)
    elif totuusarvo2 == True and totuusarvo1 == False:
        esteet[y][x] = (totuusarvo1, counter)
        return (totuusarvo2, counter2)
    else: 
        esteet[y][x] = (True, min(counter1, counter2))
        return (True, min(counter1, counter2))
   
if __name__ == "__main__":
    r = ["....@",
         "@##@#",
         ".##@#",
         "....#",
         "@@@.."]
    
    print(count(r)) # 1
 

    