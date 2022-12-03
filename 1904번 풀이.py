num = int(input())

dp = [0, 1, 2]

for i in range(3, num+1):
    new = dp[i-2] + dp[i-1]
    dp.append(new %15746)

print(dp[num])