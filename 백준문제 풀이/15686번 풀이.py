from itertools import combinations
import sys

input = sys.stdin.readline

n , m = map(int, input().split())
board = [list(map(int, input().split())) for f in range(n)]
result = 999999999
c = []
h = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            c.append([i, j])
        elif board[i][j] == 1:
            h.append([i, j])

for chi in combinations(c, m):
    l1 = 0
    for k in h:
        temp_c = 9999999
        for j in range(m):
            temp_c = min(temp_c, abs(k[0] - chi[j][0]) + abs(k[1]- chi[j][1]))
        l1 += temp_c
    result = min(result, l1)

print(result)