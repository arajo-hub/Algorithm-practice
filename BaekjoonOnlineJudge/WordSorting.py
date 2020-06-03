import sys

words=[]

for i in range(int(sys.stdin.readline())): # 몇 개의 단어를 입력할 것인지 입력한다.
    word=sys.stdin.readline().strip() # 단어를 입력하고,
    if (len(word), word) in words: # 그 단어가 이미 입력한 단어라면
        pass # 그냥 지나간다.
    else: # 그 단어가 처음 입력하는 단어라면
        words.append((len(word), word)) # (그 단어의 길이, 단어) 형태로 리스트에 넣어준다.

words.sort() # 이 때, sort()는 (길이, 단어)에서 길이를 기준으로 정렬한 후에 길이가 같다면 단어를 기준으로 정렬한다.

for leng, voca in words: # 리스트에 들어있는 정렬된 (길이, 단어)를 차례로 출력한다.
    print(voca)