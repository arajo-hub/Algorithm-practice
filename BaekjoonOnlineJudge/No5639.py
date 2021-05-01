import sys

sys.setrecursionlimit(10**9)
# 알아두자! 만약 재귀를 사용해서 풀어야 한다면 이 코드를 필수로 써야 한다고 한다.
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은데,
# 재귀로 문제를 풀 경우 이 제한에 걸리기 때문이다.
# https://fuzzysound.github.io/sys-setrecursionlimit

def f(start, end):
    if start > end: # start가 end를 넘으면 끝난 것.
        return
    else: # 아직 진행하는 중이라면.
        root = pre[start]
        div = end + 1
        for pos in range(start+1, end+1):
            if root < pre[pos]:
                div = pos
                break
        f(start+1, div-1)
        f(div, end)
        print(root)

pre = []

while True:
    try:
        # 전위순회한 결과를 입력
        pre.append(int(sys.stdin.readline()))
    except:
        break

if pre:
    f(0, len(pre)-1)

# 출처 : https://chinpa.tistory.com/17