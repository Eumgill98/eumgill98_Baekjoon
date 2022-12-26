import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    temp = True
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')' or i == ']':
            if not stack:
                temp = False
                break

            else:
                if stack[-1] == '(' and i == ')' or stack[-1] == '[' and i == ']':
                    stack.pop()
                else:
                    temp = False
                    break

    if not stack and temp:
        print('yes')
    else:
        print('no')

