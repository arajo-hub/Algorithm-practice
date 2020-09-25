from bisect import bisect_left, bisect_right
# bisect는 정렬된 리스트에 요소를 삽입할 때, 맞는 위치를 찾아 정렬 상태를 유지한 채 삽입해준다.
# 원하는 숫자의 위치를 찾았다면 그 숫자의 왼쪽에 삽입할 것인지, 오른쪽에 삽입할 것인지 정해야 하는데,
# 그럴 때 bisect_left, bisect_right를 사용한다.
# 찾는 값이 리스트 안에 있다면 bisect_left는 그 값의 index를(그 값의 왼쪽에 들어가야 하므로), bisect_right는 그 값의 직후 index를 반환한다.
# 예를 들자면,
# bisect_left([1, 2, 4, 6, 7], 4) 이라면 찾는 값 4의 index인 2를 반환하고,
# bisect_right([1, 2, 4, 6, 7], 4) 이라면 찾는 값 4의 index인 2 직후인 3을 반환한다.
# 만약 찾는 값만 3으로 바꾼다면 두 경우 모두 2를 반환한다.

def count_by_range(a, left_value, right_value):
    right_index=bisect_right(a, right_value)
    left_index=bisect_left(a, left_value)
    return right_index-left_index # a 문자열에서 left_value, right_value를 찾아 그 인덱스의 차를 구하면 개수를 구할 수 있다.

array=[[] for _ in range(10001)]
reversed_array=[[] for _ in range(10001)]

def solution(words, queries):
    answer=[]
    for word in words: # 입력받은 단어들을 각각 나누어 array와 reversed_array에 넣는다.(index는 단어의 길이)
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    print(array)
    print(reversed_array)

    for i in range(10001): # 이진탐색을 위해 각 단어들을 정렬한다.
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0]!='?': # 접미사에 와일드카드가 있을 경우
            res=count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            # array의 q와 길이가 같은 단어묶음에서 q의 ?를 a로 바꾼 값과 ?를 z로 바꾼 값의 인덱스를 각각 찾아 차를 구해 개수를 반환한다.
            # left_value에 ?를 a로 바꾼 값이 들어가고, right_value에 ?를 z로 바꾼 값이 들어가는 이유는
            # 위에서 이진탐색을 위해 각 단어들을 정렬하면서 a~z순서로 정렬되었기 때문이다.
            # a로 바꾼 값을 찾아 인덱스를 반환하고, z로 바꾼 값을 찾아 인덱스를 반환하게 되면 두 인덱스의 차는 공통된 단어의 개수가 된다.
        else: # 접두사에 와일드카드가 있을 경우
            res=count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            # array를 뒤집은 reversed_array에서 뒤집은 q의 ?를 a로 바꾼 값과 ?를 z로 바꾼 값의 인덱스를 각각 찾아 차를 구해 개수를 반환한다.

        answer.append(res)

    return answer