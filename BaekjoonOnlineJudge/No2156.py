import sys

n=int(sys.stdin.readline())
wine=[0]

for i in range(n):
    wine.append(int(sys.stdin.readline())) # 와인이 담긴 양을 넣은 리스트를 만든다.

drink=[0]
drink.append(wine[1]) # 첫번째 잔은 항상 마시므로 wine[1]을 drink에 추가해준다.

if n>1:
    drink.append(wine[1]+wine[2]) # drink에 첫번째잔과 두번째잔을 합친 값을 추가한다. 이렇게되면 drink[0]에는 0, drink[1]에는 첫번째 잔까지 마신 양, drink[2]에는 두번째 잔까지 마신 양이 저장된다.

for j in range(3, n+1): # 3번째 잔부터 n번째 잔까지는 아래와 같다.
    drink.append(max(drink[j-1], drink[j-3]+wine[j-1]+wine[j], drink[j-2]+wine[j]))
    # (전의 잔, 전전전잔째까지 마신 양+전잔의 양+지금잔(세 잔을 연속으로 마실 수는 없으므로), 혹은 전전잔까지 마신 양+지금잔) 중 제일 큰 값을 drink에 추가한다.

print(drink[n])