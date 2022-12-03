from collections import deque

def bfs(start, finish, stone, n):
    q = deque()
    q.append(start - 1)
    visited = [-1] * n
    visited[start-1] = 0

    while q :
        node = q.popleft()
        for i in range(n):
            if (i-node) % stone[node] == 0 and visited[i] == -1:
                q.append(i)
                visited[i] = visited[node] + 1
                if i == finish-1:
                    return visited[i]
    return -1

n = int(input())
stone = list(map(int, input().split()))
start, finish = map(int, input().split())
print(bfs(start, finish, stone, n))
