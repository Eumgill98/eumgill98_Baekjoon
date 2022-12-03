import sys
input = sys.stdin.readline
num = int(input())
expect =[]
for _ in range(num):
    expect.append(int(input()))

expect.sort()

result = 0
for i in range(1, num+1):
    result += abs(i - expect[i-1])

print(result)