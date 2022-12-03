import sys
input = sys.stdin.readline

num = list(input().strip())
num.sort(reverse=True)

sum = 0

if '0' not in num:
    print(-1)
else:
    for i in num:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print(''.join(num))