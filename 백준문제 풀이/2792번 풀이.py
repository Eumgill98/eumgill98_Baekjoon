import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jl = []
for _ in range(m):
    j = int(input())
    jl.append(j)

start = 1
end = max(jl)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for j in jl:
        if j % mid  == 0:
            total += j // mid
        else:
            total += (j//mid) + 1

    if total > n:
        start = mid + 1

    else:
        end = mid - 1

print(start)