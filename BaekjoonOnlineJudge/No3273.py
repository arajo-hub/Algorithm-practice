import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    X = int(input())
    arr.sort()
    left, right = 0, N - 1
    ans = 0

    while left < right:
        tmp = arr[left] + arr[right]
        if tmp == X: ans += 1
        if tmp < X:
            left += 1
            continue
        right -= 1
    print(ans)

# 출처 : https://baby-ohgu.tistory.com/12