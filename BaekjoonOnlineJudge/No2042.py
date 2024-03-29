import sys
input = sys.stdin.readline
 
# 세그먼트 트리 생성
def init(node, start, end): 
    # node가 leaf 노드인 경우 배열의 원소 값을 반환.
    if start == end :
        tree[node] = l[start]
        return tree[node]
    else :
        # 재귀함수를 이용하여 왼쪽 자식과 오른쪽 자식 트리를 만들고 합을 저장.
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]
 
# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def subSum(node, start, end, left, right) :
    
    # 겹치지 않기 때문에, 더 이상 탐색을 이어갈 필요가 없다.    
    if left > end or right < start :
        return 0
 
    # 구해야하는 합의 범위는 [left, right]인데, [start, end]는 그 범위에 모두 포함되고
    # 그 node의 자식도 모두 포함되기 때문에 더 이상 호출을 하는 것은 비효율적이다.
    if left <= start and end <= right :
        return tree[node]
 
    # 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야한다.
    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2 + 1, (start+end)//2+1, end, left, right)
 
 
def update(node, start, end, index, diff) :
 
    if index < start or index > end :
        return
 
    tree[node] += diff
    
    # 리프 노드가 아닌 경우에는 자식도 변경해줘야 하기 때문에 검사해야함.
    if start != end :
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)
 
# 수의 개수 N, 수의 변경이 일어나는 횟수 M, 구간의 합을 구하는 횟수 K
N, M, K = map(int, input().rstrip().split())
 
l = []
tree = [0] * 3000000
 
for _ in range(N) :
    l.append(int(input().rstrip()))
 
init(1, 0, N-1)
 
for _ in range(M+K) :
    # 세 개의 정수
    a, b, c = map(int, input().rstrip().split())
 
    # a가 1이면 b번째 수를 c로 바꾸고,
    if a == 1 :
        b = b-1
        diff = c - l[b]
        l[b] = c
        update(1, 0, N-1, b, diff)
    # a가 2이면 b번째 수부터 c번째 수까지의 합을 구할 것.
    elif a == 2 :                
        print(subSum(1, 0, N-1 ,b-1, c-1))

# 출처 : https://upcount.tistory.com/12