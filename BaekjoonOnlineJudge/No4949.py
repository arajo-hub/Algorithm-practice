import sys

while (True):
    string=sys.stdin.readline().strip('\n')
    if string==".":
        break

    stack=[]

    loop=True
    for i in string:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                loop=False
                break
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                loop=False
                break
    
    if string==".":
        break
    print("yes" if loop and not(stack) else "no")