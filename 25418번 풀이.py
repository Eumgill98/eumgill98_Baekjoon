import sys
input= sys.stdin.readline

a, k = map(int, input().split())

#뒤로 가볼 까?
count = 0
while k != a:
    if k % 2 == 0 and k >= a*2:
        k /= 2
    else:
        k -= 1
    count += 1



print(count)