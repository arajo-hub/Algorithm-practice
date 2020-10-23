# import sys

# N=int(sys.stdin.readline())
# numslist=[int(sys.stdin.readline()) for _ in range(N)]

# # 퀵 정렬(내림차순)
# def QuickSort(list):
#     if len(list)<=1:
#         return list

#     pivot=list[0] # pivot은 기준이 되는 값이라고 생각하면 된다. 우선은 편의상 첫번째 요소를 pivot으로 하고,
#     tail=list[1:] # 두번째 요소부터를 tail로 한다.

#     # 이제 우리가 가지고 있는 list를 pivot보다 크냐 작으냐에 따라 left와 right에 넣어준다.
#     left=[x for x in tail if x>pivot] # pivot보다 작은 값들은 왼쪽에,
#     right=[x for x in tail if x<=pivot] # pivot보다 큰 값들은 오른쪽에.

#     # left와 right가 만들어졌다면 재귀함수를 이용하여 left와 right를 또 각각 정렬시켜준다.
#     return QuickSort(left)+[pivot]+QuickSort(right)

# # 계수(Count) 정렬(내림차순)
# def CountSort(list):
#     result=[]
#     cnt=[0]*(max(list)+1) # list의 최댓값을 길이로 하는 리스트를 만들어준다.

#     for i in range(len(list)):
#         cnt[list[i]]+=1 # list에 있는 값을 위치값으로 하여 1을 넣어준다. 예를 들어, 3이 있다면 [0, 0, 0, 1]이 된다.
#     # 위 과정이 완료되면 우리의 list에 어떤 값이 몇 번 등장하는지 cnt를 보고 알 수 있다.

#     for i in range(len(cnt)-1, 0, -1): # cnt를 처음부터 끝까지 훑으면서
#         for j in range(cnt[i]): # cnt에 있는 값(=같은 값이 몇 번 등장하는지)만큼
#             result.append(i) # result에 넣어준다.

#     return result

# # 제일 간단한 방법은 파이썬 기본 정렬 라이브러리를 이용하는 것
# std_numslist=sorted(numslist, reverse=True)
# print(*std_numslist)

# 2020년 10월 23일 풀이

def boubleSort(list):
    if len(list)<=1:
        return list
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1]=list[j+1], list[j]
    return list

def selectSort(list):
    if len(list)<=1:
        return list
    for i in range(len(list)): # 리스트에서 숫자 하나를 고르고
        for j in range(i+1, len(list)): # 그 숫자 다음의 숫자들과 비교한다.
            if list[i]<list[j]: # 제일 앞에 있는 수가 비교하는 수보다 크다면
                list[i], list[j]=list[j],list[i] # 교체한다.
    return list

def quickSort(list):
    if len(list)<=1:
        return list
    pivot=list[0]
    tail=list[1:]
    left_side=[x for x in tail if x> pivot]
    right_side=[x for x in tail if x<= pivot]
    
    return quickSort(left_side)+[pivot]+quickSort(right_side)

def insertSort(list):
    if len(list)<=1:
        return list
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j]>list[j-1]:
                list[j], list[j-1]=list[j-1], list[j]
            else:
                break
    return list

def mergeSort(list):
    if len(list)>1:
        middle=len(list)//2
        left=list[:middle]
        right=list[middle:]

        mergeSort(left)
        mergeSort(right)

        i = j = k= 0

        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                list[k]=left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1

        return list

def countSort(list):
    result=[]
    cnt=[0]*(max(list)+1)

    for i in range(len(list)):
        cnt[list[i]]+=1

    for i in range(len(cnt)-1, 0, -1):
        for j in range(cnt[i]):
            result.append(i)

    return result
        
import sys

n=int(sys.stdin.readline())

list=[]
for i in range(n):
    list.append(int(sys.stdin.readline()))

# print(boubleSort(list))
# print(selectSort(list))
# print(quickSort(list))
# print(insertSort(list))
# print(mergeSort(list))
# print(countSort(list))

list=sorted(list, reverse=True)
print(*list)