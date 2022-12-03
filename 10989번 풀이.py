total =[]
for i in range(int(input())):
    num = int(input())
    total.append(num)

total = sorted(total)
for j in total:
    print(j)