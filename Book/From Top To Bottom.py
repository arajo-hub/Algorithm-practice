import sys

N=int(sys.stdin.readline())
numslist=[int(sys.stdin.readline()) for _ in range(N)]

# 퀵 정렬(내림차순)
def QuickSort(array):
    if len(array)<=1:
        return array

    pivot=array[0] # pivot은 기준이 되는 값이라고 생각하면 된다. 우선은 편의상 첫번째 요소를 pivot으로 하고,
    tail=array[1:] # 두번째 요소부터를 tail로 한다.

    # 이제 우리가 가지고 있는 array를 pivot보다 크냐 작으냐에 따라 left와 right에 넣어준다.
    left=[x for x in tail if x>pivot] # pivot보다 작은 값들은 왼쪽에,
    right=[x for x in tail if x<=pivot] # pivot보다 큰 값들은 오른쪽에.

    # left와 right가 만들어졌다면 재귀함수를 이용하여 left와 right를 또 각각 정렬시켜준다.
    return QuickSort(left)+[pivot]+QuickSort(right)

# 계수(Count) 정렬(내림차순)
def CountSort(array):
    result=[]
    cnt=[0]*(max(array)+1) # array의 최댓값을 길이로 하는 리스트를 만들어준다.

    for i in range(len(array)):
        cnt[array[i]]+=1 # array에 있는 값을 위치값으로 하여 1을 넣어준다. 예를 들어, 3이 있다면 [0, 0, 0, 1]이 된다.
    # 위 과정이 완료되면 우리의 array에 어떤 값이 몇 번 등장하는지 cnt를 보고 알 수 있다.

    for i in range(len(cnt)-1, 0): # cnt를 처음부터 끝까지 훑으면서
        for j in range(cnt[i]): # cnt에 있는 값(=같은 값이 몇 번 등장하는지)만큼
            result.append(i) # result에 넣어준다.

    return result

# 제일 간단한 방법은 파이썬 기본 정렬 라이브러리를 이용하는 것
std_numslist=sorted(numslist, reverse=True)
print(*std_numslist)