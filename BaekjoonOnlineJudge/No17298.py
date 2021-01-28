import sys

n=int(sys.stdin.readline()) # 수열의 크기

array=list(map(int, sys.stdin.readline().split()))

stack = []
result = [-1 for _ in range(n)]

# 스택에 인덱스 넣는다는 것에 주의!

for i in range(len(array)):
    try:
        while array[stack[-1]] < array[i]:
            result[stack.pop()] = array[i]
    except:
        pass
        
    stack.append(i) # 스택이 비어있으면 넣어준다.
        
print(*result)