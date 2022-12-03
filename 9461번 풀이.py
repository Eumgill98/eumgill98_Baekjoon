
for i in range(int(input())):
    dp = [0,1,1]
    num = int(input())
    for j in range(3, num+1):
        dp.append(dp[j-3] + dp[j-2])
    print(dp[num])