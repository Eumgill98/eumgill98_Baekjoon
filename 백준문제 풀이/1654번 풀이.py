import sys
input = sys.stdin.readline

k, n = map(int, input().split())
LAN_LIST = []
for _ in range(k):
    LAN_LIST.append(int(input()))

start = 1
end = max(LAN_LIST)

while start <= end:
    mid = (start + end) //2
    total = sum(f // mid for f in LAN_LIST)

    if total >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1


print(result)