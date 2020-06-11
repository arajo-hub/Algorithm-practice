def solution(n, lost, reserve):
    answer = 0
    students=[1]*n
    for i in range(1, n+1):
        if i in lost and i not in reserve:
            students[i-1]=0
        elif i in lost and i in reserve:
            students[i-1]=1
        elif i not in lost and i in reserve:
            students[i-1]=2

    for j in lost:
        if students[j-1]==1:
            pass
        else:
            if j==len(students):
                if students[j-2]==2:
                    students[j-2]=1
                    students[j-1]=1
            elif j==1:
                if students[j]==2:
                    students[j]=1
                    students[j-1]=1
            else:
                if students[j-2]==2:
                    students[j-2]=1
                    students[j-1]=1
                elif students[j]==2:
                    students[j]=1
                    students[j-1]=1

    answer=n-students.count(0)
    return answer

# print(solution(5, [2, 4], [1, 3, 5]))
print(solution(6, [1, 3, 5], [2, 4, 6]))
# print(solution(5, [2, 4, 5], [1, 3]))