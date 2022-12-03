import sys
n,c = map(int, sys.stdin.readline().split())
k = [0]*(c+1)
for i in range(n):
    cnt = int(sys.stdin.readline())
    if cnt==1:
        print(c)
        quit()
    for j in range(cnt, c+1, cnt):
        k[j] = 1
print(sum(k))