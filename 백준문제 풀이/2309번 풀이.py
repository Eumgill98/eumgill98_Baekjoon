import sys
import random
#9명의 키 받기
total =[]
for _ in range(9):
    tall = int(sys.stdin.readline())
    total.append(tall)

#키의 합이 100이 될 때까지 while 문 돌리기
while True:
    numbers=random.sample(total, 7)
    sum_key = 0
    for i in numbers:
        sum_key += i

    if sum_key == 100:
        break

numbers.sort()
for k in numbers:
    print(k)

