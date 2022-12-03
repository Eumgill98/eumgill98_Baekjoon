#이항계수 문제
# 5 2 -> 5!/(5-2)!*2!
## 이식을 알고리즘으로 구현 하는 것이 목표

def factorial(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    return total

a,b = map(int, input().split())
print(factorial(a)//(factorial(a-b)*factorial(b)))

