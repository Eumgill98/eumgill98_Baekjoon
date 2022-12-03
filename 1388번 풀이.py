def dfs(x,y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        for s in [1, -1]:
            Y = y + s
            if (Y > 0 and Y < m) and graph[x][Y] == '-':
                dfs(x, Y)
    if graph[x][y] == '|':
        graph[x][y] =1
        for f in [1, -1]:
            X = x + f
            if (X > 0 and X < n) and graph[X][y] == '|':
                dfs(X, y)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(f for f in input()))

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != 1:
            dfs(i,j)
            count+=1
print(count)