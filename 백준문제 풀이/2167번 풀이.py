n, m = map(int, input().split())
a= []
df =[[0]*(m+1) for _ in range(n+1)]
for _ in range(n):
    a.append((list(map(int, input().split()))))

for i in range(1, n+1):
    for j in range(1, m+1):
        df[i][j] = a[i-1][j-1] + df[i][j - 1] + df[i - 1][j] - df[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i,j,x,y = map(int, input().split())
    print(df[x][y] - df[x][j - 1] - df[i - 1][y] + df[i - 1][j - 1])