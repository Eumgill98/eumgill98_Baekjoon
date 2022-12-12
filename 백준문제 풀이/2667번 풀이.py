from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(graph, x, y):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt


c = [bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

c.sort()
print(len(c))
print(*c, sep='\n')



""" dfs 풀이

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언
count = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 한 점을 기준으로 (위 아래 왼쪽 오른쪽) 으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global count

    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


# 그래프의 원소가 1일때만 dfs로 집을 방문한다.
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0
            
result.sort()           
print(len(result))
print(*result, sep='\n')
"""