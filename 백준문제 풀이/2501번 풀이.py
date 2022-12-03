import sys

N, K = map(int, sys.stdin.readline().split())
last_list = []

for i in range(1, N+1):
    if N % i== 0:
        last_list.append(i)


if len(last_list) >=K:
    print(last_list[K-1])
else:
    print(0)



"""
n,k=map(int,input().split());print(*[i for i in range(1,1+n)if n%i<1][k-1:k]or[0])
"""