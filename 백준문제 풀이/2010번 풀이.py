import sys

num = int(sys.stdin.readline())
total = 0

for i in range(num):
    mult = int(sys.stdin.readline())
    total+= mult

print(total-(num-1))
