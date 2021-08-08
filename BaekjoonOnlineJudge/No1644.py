import math

n = int(input())

prime_number = []
array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2

        while i * j <= n:
            array[i * j] = False
            j += 1

for num in range(2, n + 1):
    if array[num]:
        prime_number.append(num)

count = 0
interval_sum = 0
end = 0

for start in range(len(prime_number)):
    while interval_sum < n and end < len(prime_number):
        interval_sum += prime_number[end]
        end += 1

    if interval_sum == n:
        count += 1
    interval_sum -= prime_number[start]

print(count)

# 출처 : https://bbbyung2.tistory.com/82