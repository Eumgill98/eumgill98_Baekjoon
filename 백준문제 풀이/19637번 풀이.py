import sys
input = sys.stdin.readline

def  binary(num):
    start = 0
    end = len(pl) - 1
    while start <= end:
        mid = (start + end )// 2
        if num > pl[mid]:
            start = mid + 1
        else:
            end = mid - 1

    print(nl[end + 1])


n, m = map(int, input().split())
pl = []
nl = []

for i in range(n):
    name, power = input().split()
    power = int(power)
    if pl and pl[-1] == power:
        continue
    pl.append(power)
    nl.append(name)

for _ in range(m):
    num = int(input())
    binary(num)