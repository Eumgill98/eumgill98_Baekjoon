import sys
total_num = int(sys.stdin.readline())
total = []

for i in range(total_num):
    x, y = map(int, sys.stdin.readline().split())
    total.append((x,y))


for i in total:
    rank = 1
    for j in total:
        if i[0] < j[0] and i[1] < j[1]:
            rank+=1
    print(rank, end= " ")