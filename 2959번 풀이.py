import sys

total=list(map(int, sys.stdin.readline().split()))
total = sorted(total)
min_total = min(total)
max_1total = total[-2]
print(min_total*max_1total)
