import sys
input = sys.stdin.readline

n = int(input())
card = [0] + [int(f) for f in input().split()]
dp = [0] * (n+1)


for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+card[j])

print(dp[n])

#dp[1] - 하나 구매 -무조건 card[1]
#dp[2] - 두개 구매 -> dp[1]+card[1] or card[2]
#dp[3] - dp[2]+card[1] or dp[1] +card[2] or d[3]

