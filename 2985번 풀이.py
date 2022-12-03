import sys
a, b, c = map(int, sys.stdin.readline().split())

if (a == b+c):
    print(f'{a}={b}+{c}')
elif (a == b-c):
    print(f'{a}={b}-{c}')
elif (a == b*c):
    print(f'{a}={b}*{c}')
elif (a == b/c):
    print(f'{a}={b}/{c}')
elif (a+b ==c):
    print(f'{a}+{b}={c}')
elif (a-b ==c):
    print(f'{a}-{b}={c}')
elif (a*b ==c):
    print(f'{a}*{b}={c}')
elif (a/b ==c):
    print(f'{a}/{b}={c}')




"""
a,b,c = map(int, input().split())
i = [a+b-c, a-b-c, a*b-c, a-b+c, a-b*c, a*c-b].index(0);
print(a, '+-*==='[i], b, '===-*/'[i], c, sep='')
x
"""