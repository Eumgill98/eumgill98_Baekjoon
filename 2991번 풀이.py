import sys

a, b, c, d = map(int, sys.stdin.readline().split())
p, m, n = map(int, sys.stdin.readline().split())
people = [p, m, n]

for i in people:
    dog = 0
    if 0 < i % (a + b) <= a:
        dog += 1
    if 0 < i % (c + d) <= c:
        dog += 1

    print(dog)




