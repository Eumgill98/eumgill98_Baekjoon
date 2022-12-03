import sys

n,k = map(int, sys.stdin.readline().split())
coin = []
for _  in range(n):
    money = int(sys.stdin.readline())
    if money <=k:
        coin.append(money)
    else:
        pass

coin = coin[::-1]

count =0
for j in coin:
    if (k // j ) <= 0:
        pass
    else:
        count += (k//j)
        k -= (j * (k//j))

print(count)
