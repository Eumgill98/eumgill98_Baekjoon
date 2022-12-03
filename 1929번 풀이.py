#소수판별 메소드
x,y = map(int, input().split())
n = y
a = [False, False] + [True] *(n-1)

sosu = []

##에라토스테네스 채
for i in range(2, n+1):
    if a[i]:
        if i >= x:
            sosu.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False


print(*sosu, sep="\n")

