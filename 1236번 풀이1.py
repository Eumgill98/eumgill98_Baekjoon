n, m = map(int,input().split())
a_list = []

for _ in range(n):
    a_list.append(input())

a, b = 0, 0


for i in range(n):
    if "X" not in a_list[i]:
        a += 1

for j in range(m):
    if "X" not in [a_list[i][j] for i in range(n)]:
        b += 1

print(max(a ,b))