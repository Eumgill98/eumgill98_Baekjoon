import sys

a, b, c = map(int, sys.stdin.readline().split())

num = b-a
num2 = c-b

total = [num, num2]

print(max(total)-1)