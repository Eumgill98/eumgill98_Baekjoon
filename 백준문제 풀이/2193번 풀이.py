def pandan(n):

    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2
    if dp[n] !=0 :
        return dp[n]
    dp[n] = pandan(n-1) + pandan(n-2)
    return dp[n]


n = int(input())
dp = [0] * (n+1)
print(pandan(n))