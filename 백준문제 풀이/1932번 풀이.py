import sys
input = sys.stdin.readline

n = int(input())
tree = []
for _ in range(n):
    values = [int(f) for f in input().split()]
    tree.append(values)


for i in range(1, n):
    for j in range(0 , i+1):
        if j == 0:
            tree[i][0] += tree[i-1][0]
        elif j == i:
            tree[i][j] += tree[i-1][j-1]
        else:
            tree[i][j] += max(tree[i-1][j-1], tree[i-1][j])


print(max(tree[n-1]))

