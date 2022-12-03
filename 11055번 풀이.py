num = int(input())
a = list(map(int, input().split()))
dp  = [a[0]] * num

for i in range(1, num):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+a[i])

print(max(dp))