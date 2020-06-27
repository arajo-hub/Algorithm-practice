import sys

T=int(sys.stdin.readline())


# 이 문제의 조건은 두 가지이다.
# 1. 괄호는 쌍을 이룰 것. ex. ()나 (())처럼.
# 2. '('괄호가 항상 먼저 나올 것. ex. ()는 True, )(는 False

def YesOrNo(strList):
    Or = 0 # 스택을 이용하는 문제였지만 정수를 사용해서 풀어도 문제가 없어서 정수를 사용했다. '('괄호가 나오면 Or+=1, ')'괄호가 나오면 Or-=1
    for j in range(len(strList)):
        if Or<0: # Or가 0보다 작을 경우, 무조건 "NO"를 리턴하는데, Or가 아직 어떤 괄호도 판별하지 않은 상태에서 ')'로 시작하면(위의 조건 2를 위배하면) 0보다 작아지기 때문.
            return "NO"
        elif j == len(strList)-1 and Or!=0: # StrList를 다 살펴보았고, Or가 0보다 크다면(='('가 남아있는 상태) 괄호는 쌍을 이루어야 한다는 조건 1이 위배되므로 "NO"를 return.
            return "NO"
        elif j == len(strList)-1 and Or==0: # StrList를 다 살펴보았고, Or가 0과 같다면(=괄호가 쌍을 이루면) "YES"를 return.
            return "YES"
        else: # StrList를 아직 살펴보고 있고 (')'가 먼저 나오지 않은) 정상적인 상황이라면,
            if strList[j] == '(': Or += 1
            if strList[j] == ')': Or -= 1

for i in range(T):
    str=sys.stdin.readline()
    print(YesOrNo(str))