def solution(S):
    answer=len(S) # 압축할 문자열이 없을 경우 S의 길이를 리턴해야하므로 answer에 저장한다.
    for j in range(1, len(S)//2+1): # # 압축할 문자열이 있을 경우, 그 문자열의 최대 길이는 S길이의 반이 되므로 len(S)//2+1이 최종값이 된다.
        strings=''
        idx=S[0:j] # 있는지 찾아볼 문자열
        cnt=1
        for i in range(j, len(S), j):
            if idx==S[i:i+j]: # 압축할 문자열이 있다면(=바로 뒤의 문자열이 idx와 같다면)
                cnt+=1 # cnt를 1 올려준다.
            else: # 압축할 문자열이 없다면(=바로 뒤의 문자열이 idx와 같지 않다면)
                strings+=str(cnt)+idx if cnt>=2 else idx # idx는 cnt가 2 이상일 때, str(cnt)+idx의 형태를 가진다. 2 이상이 아닐 때는 그냥 idx가 된다.
                idx=S[i:i+j] # idx는 압축할 문자열을 못 찾은 그 이후의 문자열이 되고
                cnt=1 # cnt는 1로 초기화해준다.
        strings+=str(cnt)+idx if cnt>=2 else idx # 나머지 부분을 압축한다.
        answer = min(answer, len(strings))
    return answer