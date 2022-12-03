def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            res[i] = res[v] + 1
            dfs(i)

n= int(input())
a, b=map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = [0]*(n+1)


for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)


dfs(a)

if res[b]>0:
    print(res[b])
else:
    print(-1)