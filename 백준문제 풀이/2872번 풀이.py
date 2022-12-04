import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    book = int(input())
    stack.append(book)

target = n
cnt = 0

for i in range(n-1, -1, -1):
    if stack[i] != target:
        cnt += 1
    else:
        target -= 1

print(cnt)