from itertools import combinations_with_replacement

n = int(input())
result = []
numbers = [1, 5, 10, 50]

for temp in combinations_with_replacement(range(4), n):
    s= 0
    for i in temp:
        s += numbers[i]
    result.append(s)


print(len(set(result)))