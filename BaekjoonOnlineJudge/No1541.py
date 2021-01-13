import sys

# 예를 들어, 아래처럼 숫자 5개를 입력한다고 하자.
# 25-32+17+8-14
# 이 경우 최솟값은
# 25-(32+17+8)-14 = 25-57-14 = -46이다.
# 식의 결과를 최솟값을 만든다는 것은 가장 큰 음수를 만든다는 것과 같다.
# 그러므로 '-'를 기준으로 식을 계산하면 된다.

equation=sys.stdin.readline().split('-')

nums=[]

# '-'를 기준으로 쪼갠 식 내부로 들어가서
for i in equation:
    count=0
    splited=i.split('+') # +를 기준으로 숫자를 나눈 후
    for each in splited:
        count+=int(each) # 그 숫자들끼리 더한다.(괄호 안의 계산)
    nums.append(count) # 그리고 nums에 그 더한 값들을 추가한다.

first=nums[0]

for j in range(1, len(nums)): # 그리고 이제 '-' 계산만 남았으므로 빼준다. (괄호 밖의 계산)
    first-=nums[j]

print(first)