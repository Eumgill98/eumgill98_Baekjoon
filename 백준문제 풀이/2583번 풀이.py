from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n, k = map(int, input().split())
s = [[0] * n for i in range(m)]
visited = [[False] * n for i in range(m)]
result = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            s[j][k] = 1


def bfs(x,y):
    c = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <=nx <m and 0<=ny <n and s[nx][ny] == 0 and visited[nx][ny] == False:
                q.append([nx,ny])
                visited[nx][ny] = True
                c += 1

    return c

for i in range(m):
    for j in range(n):
        if s[i][j] == 0 and visited[i][j] == False:
            result.append(bfs(i,j))

print(len(result))
print(*sorted(result))