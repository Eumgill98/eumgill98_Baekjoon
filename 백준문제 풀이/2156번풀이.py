import sys
input = sys.stdin.readline

num = int(input())
v = [0] * 10001
dp = [0] * 10001
for i in range(1, num+1):
    v[i] = int(input())

dp[1] = v[1]
dp[2] = v[1] + v[2]

for j in range(3, num+1):
    dp[j] = max(dp[j-1], dp[j-3]+v[j-1]+ v[j], dp[j-2] + v[j])

print(dp[num])
