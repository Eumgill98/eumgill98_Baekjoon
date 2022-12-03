import sys
import math
a, b, c = map(int, sys.stdin.readline().split())

day = (((c-a)/(a-b)) + 1)
print(math.ceil(day))