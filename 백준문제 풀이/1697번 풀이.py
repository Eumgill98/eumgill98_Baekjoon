import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(n)

    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for n_x in (v-1, v+1, v*2):
            if 0<= n_x < MAX and  not visited[n_x]:
                visited[n_x] = visited[v] + 1
                q.append(n_x)


MAX = 100001
n, k = map(int,input().split())
visited = [0] * MAX
print(bfs())