import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()


    cnt = 0
    result = 0

    for i in range(n):
        while True:
            if cnt == m or a[i] <= b[cnt]:
                result += cnt
                break

            else:
                cnt += 1

    print(result)
