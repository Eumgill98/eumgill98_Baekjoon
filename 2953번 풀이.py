import sys
total = []
for i in range(5):
    total.append(sum([int(f) for f in sys.stdin.readline().split()]))
print((total.index(max(total))+1), max(total))