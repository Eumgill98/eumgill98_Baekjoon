total_money = int(input())

money =0
for i in range(int(input())):
    a, b = map(int, input().split())
    money += a*b

if total_money == money:
    print('Yes')
else:
    print('No')