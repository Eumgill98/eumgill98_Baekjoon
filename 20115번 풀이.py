import sys
input = sys.stdin.readline

num = int(input())
drink = list(map(int, input().split()))

drink.sort(reverse=True)

count = drink[0]

for i in range(1, num):
    count+= drink[i] / 2

print("%g" % count)