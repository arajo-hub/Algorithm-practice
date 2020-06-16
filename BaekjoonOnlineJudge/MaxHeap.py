import sys
import heapq

heap=[]

for i in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    if num==0:
        if heap==[]:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-num, num)) # heappop은 최소값을 꺼내는 함수.
        # 그렇기 때문에 최대값을 꺼내려면 heap에 (-num, num)형태로 저장해서 -num을 인덱스삼아 최대값을 찾은 다음, num으로 최대값을 출력한다.