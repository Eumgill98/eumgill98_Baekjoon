import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))

stack = []
stack.append([1, top[0]])
res = [0]

for i in range(1, n):
    while stack:
        if stack[-1][1] >= top[i]:
            res.append(stack[-1][0])
            stack.append([i+1, top[i]])
            break
        else:
            stack.pop()

    if not stack:
        res.append(0)
        stack.append([i+1, top[i]])

print(*res, end=' ')

