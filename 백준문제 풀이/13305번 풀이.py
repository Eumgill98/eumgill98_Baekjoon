n = int(input())

road = list(map(int, input().split()))
money = list(map(int, input().split()))

min_money = 0
m = money[0]

for i in range(n-1):
    if money[i] < m:
        m = money[i]
    min_money += m * road[i]

print(min_money)