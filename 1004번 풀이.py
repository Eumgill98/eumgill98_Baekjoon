import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    hang = int(input())
    for _ in range(hang):
        px, py, pr = map(int, input().split())
        d1 = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5
        d2 = (((x2 - px) ** 2) + ((y2 - py) ** 2)) ** 0.5
        if (d1 < pr and d2 > pr) or (d1 > pr and d2 < pr):
            cnt += 1
    print(cnt)

