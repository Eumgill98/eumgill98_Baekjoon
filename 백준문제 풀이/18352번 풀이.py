import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

#bfs
queue =  deque()
queue.append(x)

while queue:
    q = queue.popleft()

    for j in graph[q]:
        if distance[j] == -1:
            distance[j] = distance[q] + 1
            queue.append(j)


if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)