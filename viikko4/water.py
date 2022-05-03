from heapq import heapify, heappush, heappop
import heapq

def count(a,b,x):
    # TODO

    heap = []
    heapify(heap)
    heappush(heap,(0,0))
    
    vierailtu = set()

    while True:
        alku, loppu = heappop(heap)
       
       
        if (alku,loppu) in vierailtu:
            continue
        vierailtu.add((alku,loppu))
        print(alku,loppu)
        if (alku or loppu) == 2:
            break
        if alku == 0:
            heappush(heap, (a,loppu))
        if loppu == 0:
            heappush(heap,(alku,b))
        if alku == a or loppu >= 0:
            if a >= b:
                siirtyva = a-(a-b)
                heappush(heap,(a-siirtyva,siirtyva))
            if b >= a:
                heappush(heap,(0,a))
        if alku >= 0 or loppu == b:
            if b >= a:
                siirtyva = b-(b-a)
                heappush(heap,(siirtyva, b-siirtyva))
            if a >= b:
                heappush(heap,(b,0))
        if alku >= 0 and loppu == b:
            heappush(heap,(alku, 0))
        if alku == a and loppu >= 0:
            heappush(heap,(0, loppu))
        
          
        
        


if __name__ == "__main__":
    print(count(5,4,2)) # 22
    print(count(4,3,2)) # 16
    print(count(3,3,1)) # -1
    print(count(10,9)) # 46
    print(count(123,456,42)) # 10530