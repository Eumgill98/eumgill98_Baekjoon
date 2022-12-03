import sys

n, m = map(list, sys.stdin.readline().split())

n = list(map(int,n))
m = list(map(int,m))

print(sum(n)*sum(m))