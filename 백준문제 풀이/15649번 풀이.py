"""import itertools
n, m = map(int, input().split())
use_number = [str(f) for f in range(1, n+1)]

total = list(map(" ".join, itertools.permutations(use_number, m)))

for j in total:
    print(j)
"""

n, m = list(map(int, input().split()))

s = []

def dfs():
    if len(s) ==m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()

