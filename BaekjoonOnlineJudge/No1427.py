# 이 문제는 하나의 수를 입력받아 그 수의 각 자리수를 내림차순으로 정렬하는 문제이다.
# 하나의 수를 각 자리수로 나누어 리스트에 저장하고, 정렬한 뒤 print해주면 되는데,
# 나는 수를 입력받아 str으로 형변환을 한 뒤, extend를 통해 리스트에 저장해주었다.
# extend함수를 이용하게 되면,
# extend => ['e', 'x', 't', 'e', 'n', 'd']의 형태로 저장된다.

num=[]
num.extend(str(int(input())))
num.sort(reverse=True)
temp=''.join(num) # join함수 기억해두기!
print(temp)