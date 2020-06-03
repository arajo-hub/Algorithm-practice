import sys

words=[]
i=0

for i in range(int(sys.stdin.readline())):
    word=sys.stdin.readline().strip()
    if word in words:
        pass
    else:
        words.append(word)

for j in words:
    words.append((len(j), j))

print(words)