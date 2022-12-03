import sys

input = sys.stdin.readline
num = int(input())
box = list(map(int, input().split()))
dp = []
dp.append(1)

for i in range(1, num):
    new = []
    for j in range(i):
        if box[i] > box[j]:
            new.append(dp[j] + 1)
    if not new:
        dp.append(1)
    else:
        dp.append(max(new))
print(max(dp))


