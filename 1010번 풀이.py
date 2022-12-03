def f(n):
    num=1
    for i in range(1, n+1):
        num *= i
    return num

for i in range(int(input())):
    n, m = map(int, input().split())
    #문제핵심 mCn을 어떻게 구현할 것인가?
    #m! / (m-n)!n!
    dari = f(m) // (f(n) * f(m-n))
    print(dari)
