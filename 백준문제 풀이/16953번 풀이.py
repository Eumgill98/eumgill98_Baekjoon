#이게 왜 너비 탐색 문제?
## How to solved using by BFS()

from collections import deque

a , b = map(int, input().split())
v = deque()
v.append((a, 1))
while v:
    c, d = v.popleft()
    if c > b:
        continue
    if c == b:
        print(d)
        break
    v.append((int(str(c)+"1"), d+1))
    v.append((c*2, d+1))

else:
    print(-1)