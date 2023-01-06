import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
inf, result = 2147000000, 2147000000

for j in range(3):
    dp = [[inf, inf, inf] for _ in range(n)]
    dp[0][j] = cost[0][j]

    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i-1][0],dp[i-1][2])
        dp[i][2] = cost[i][2] + min(dp[i-1][0],dp[i-1][1])


    for i in range(3):
        if j != i:
            result = min(result, dp[-1][i])

print(result)