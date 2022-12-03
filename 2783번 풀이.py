import sys
total = []
X, Y = map(int, sys.stdin.readline().split())
seven= X / Y
total.append(seven)

N = int(sys.stdin.readline())
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    not_seven = x / y
    total.append(not_seven)

min_cost = min(total)*1000
print(f"{min_cost:.2f}")