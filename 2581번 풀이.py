import sys
m= int(sys.stdin.readline())
n= int(sys.stdin.readline())

total = []
for i in range(m, n+1):
    for j in range(2, i+1):
        if j == i:
            total.append(i)
        if i % j == 0:
            break


if not total:
    print(-1)

else:
    print(sum(total))
    print(total[0])