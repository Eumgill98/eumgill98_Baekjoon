#문제의 핵심 : 문자열로 받은 숫자를 어떻게 나눌 것인가 하는 문제 (인덱싱의 문제)
import math
num = input()
result = []

for i in range(1, len(num)):
    a = [int(f) for f in num[:i]]
    b = [int(f) for f in num[i:]]
    if math.prod(a) == math.prod(b):
        print('YES')
        result.append(a)
        exit()


if result==[]:
    print('NO')


##숏코딩
"""
a=input()
for i in range(1,len(a)):
 if eval('*'.join(a[:i])+'=='+'*'.join(a[i:])):print('YES');exit(0)
print('NO')
"""

