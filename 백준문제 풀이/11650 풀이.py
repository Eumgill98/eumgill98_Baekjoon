
total =[]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    total.append([x,y])

total = sorted(total)
for j in range(n):
    print(total[j][0], total[j][1])