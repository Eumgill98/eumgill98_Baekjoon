import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))


stack = []
res = [-1 for i in range(n)]

for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        res[stack.pop()] = A[i]

    stack.append(i)


print(*res)

