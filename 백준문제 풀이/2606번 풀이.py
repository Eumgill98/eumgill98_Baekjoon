## 깊이 탑색 , 너비 탐색

#그래프 생성
n = int(input())
v = int(input())

graph = [[] for i in range(n+1)] #그래프 초기화
vis = [0]*(n+1)

for i in range(v):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    vis[v] = 1
    for nx in graph[v]:
        if vis[nx] ==0:
            dfs(nx)


dfs(1)
print(sum(vis)-1)