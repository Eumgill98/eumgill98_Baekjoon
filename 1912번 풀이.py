
num = int(input())
n = list(map(int, input().split()))


for i in range(1, num):
    n[i] = max(n[i], n[i-1] + n[i])

print(max(n))