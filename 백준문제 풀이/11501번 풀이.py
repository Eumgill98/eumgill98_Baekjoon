import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    day = int(input())
    stock = list(map(int, input().split()))

    cnt = 0
    max_v = 0

    for i in range(len(stock)-1, -1, -1):
        if stock[i] > max_v:
            max_v = stock[i]
        else:
            cnt += max_v - stock[i]

    print(cnt)