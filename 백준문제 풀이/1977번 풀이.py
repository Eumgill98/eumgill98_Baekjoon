import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

total = []
for i in range(m, n+1):
    num_root =  int(i**0.5)
    if i == num_root **2:
        total.append(i)

if total ==[]:
    print(-1)
else:
    print(sum(total))
    print(min(total))
