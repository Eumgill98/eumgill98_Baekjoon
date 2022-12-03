dp = [0 for f in range(0, 251)]
while True:
    try:
        num = int(input())
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3

        for i in range(3, num+1):
            dp[i] = (dp[i-1] + (2*dp[i-2]))
        print(dp[num])
    except:
        break

