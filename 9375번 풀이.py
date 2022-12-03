from collections import Counter

num = int(input())

for _ in range(num):
    c_n = int(input())
    total = []
    for _ in range(c_n):
        cloth, what = map(str, input().split())
        total.append(what)
    total_c = list(Counter(total).values())
    count = 1

    for k in total_c:
        count *= k+1

    print(count-1)




