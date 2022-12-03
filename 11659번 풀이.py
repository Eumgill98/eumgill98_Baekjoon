## 누적합 (prefix sum)알고리즘을 이용한 풀이
import sys

n,m = map(int, sys.stdin.readline().split())
pfs = list(map(int, sys.stdin.readline().split()))

for i in range(n-1):
    pfs[i+1] += pfs[i]

pfs = [0] + pfs ## 0인덱스 추가

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    print(pfs[j] - pfs[i-1])
    print(pfs[j] - pfs[i-1])