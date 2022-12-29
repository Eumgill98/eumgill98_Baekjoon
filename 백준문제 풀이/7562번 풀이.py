from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(c_x, c_y, t_x, t_y):
    q = deque()
    q.append([c_x, c_y])
    s[c_x][c_y] = 1
    while q:
        a, b = q.popleft()
        if a == t_x and b == t_y:
            print(s[t_x][t_y] -1)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < l and 0<= y < l and s[x][y] == 0:
                q.append([x, y])
                s[x][y] = s[a][b] + 1

for _ in range(int(input())):
    l = int(input())
    c_x, c_y = map(int, input().split())
    t_x, t_y = map(int, input().split())

    s = [[0] * l for i in range(l)]
    bfs(c_x, c_y, t_x, t_y)
