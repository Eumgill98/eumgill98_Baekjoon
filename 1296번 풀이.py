yeo = input()
N = int(input())
max_key, max_values = 0, 0
new_name = sorted([input() for i in range(N)])
for i in range(N):
    L = yeo.count('L') + new_name[i].count('L')
    O = yeo.count('O') + new_name[i].count('O')
    V = yeo.count('V') + new_name[i].count('V')
    E = yeo.count('E') + new_name[i].count('E')
    total = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    if max_values < total:
        max_key = i
        max_values=total

print(new_name[max_key])