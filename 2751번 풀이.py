import sys

total = []

for i in range(int(sys.stdin.readline())):
    total.append(int(sys.stdin.readline()))

total = sorted(total)

for j in total:
    print(j)