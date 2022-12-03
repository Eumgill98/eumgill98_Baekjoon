"""
import sys
num = int(sys.stdin.readline())
total = []

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    k = str(a ** b)[-1]
    if k == '0':
        k = '10'
    total.append(k)

for i in total:
    print(i)
"""


## 1차 시도 시간초과
total = []
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    new_b = b % 4  # 모든 제곱은 4번의 순환을 가짐.
    if new_b == 0:  # 만약 4번째라면(1,2,3은 그대로 값이 저장되나 4는 0으로 저장됨)
        new_b = 4  # 그 값을 4로 바꿔준다.
    number = a ** new_b
    if number % 10 == 0:  # 계산한 값의 일의자리가 0이라면
        total.append(10)  # 10을 출력
    else:  # 1~9 사이라면
        total.append(number % 10) #1~9 출력

for j in total:
    print(j)