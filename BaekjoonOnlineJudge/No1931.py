import sys

n=int(sys.stdin.readline()) # 회의실의 개수

time=[]

for i in range(n):
    time.append(list(map(int, sys.stdin.readline().split()))) # [회의 시작 시간, 끝나는 시간]

time.sort(key=lambda x : (x[1], x[0])) # 끝나는 시간과 시작하는 시간 모두 오름차순으로 정리 -> 가장 일찍 시작하면서 가장 빨리 끝나는 회의부터 시작.

count=1
end_time=time[0][1]
for j in range(1, n):
    if time[j][0]>=end_time: # 그전 회의가 끝난 시간 이후에 시작되는 회의를 찾는다.
        count+=1
        end_time=time[j][1]

print(count)