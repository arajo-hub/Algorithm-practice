import sys

N, M=map(int, sys.stdin.readline().split())
# N은 나무의 수, M은 상근이가 집으로 가져가려고 하는 나무의 길이

tree=list(map(int, sys.stdin.readline().split()))

start=1
end=max(tree)

while (start<=end):
    mid=(start+end)//2
    result=0
    for i in tree:
        if i>mid:
            result+=(i-mid)
    if result>=M:
        start=mid+1
    else:
        end=mid-1

print(end)