import sys
input = sys.stdin.readline

n,m = map(int, input().split())
candy = [list(map(int, input().split())) for f in range(n)]

for i in range(1, m):
    candy[0][i] += candy[0][i-1]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            candy[i][j] += candy[i-1][j]
        else:
            candy[i][j] += max(candy[i-1][j], candy[i-1][j-1],candy[i][j-1])
print(candy[-1][-1])


