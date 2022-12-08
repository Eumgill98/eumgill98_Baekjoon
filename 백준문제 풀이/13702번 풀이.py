import sys
input = sys.stdin.readline

n, k = map(int, input().split()) #주전자 #사람수
m = []
for _ in range(n):
    m.append(int(input()))

start = 1
end = max(m)

while start <= end:
    mid = (start + end) // 2

    can = sum(f // mid for f in m)

    if can >= k:
        start = mid +1
        answer = mid
    else:
        end = mid - 1

print(answer)

