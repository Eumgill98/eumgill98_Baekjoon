import sys
total  = []

for i in range(int(sys.stdin.readline())):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    total.append((age, name))

total = sorted(total, key = lambda x : x[0])

for j in total:
    print(j[0], j[1])