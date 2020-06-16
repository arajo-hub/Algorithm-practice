import sys
import heapq

heap=[]

for i in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    if num==0:
        if heap==[]:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)