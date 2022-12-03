import sys

a, b = map(int, sys.stdin.readline().split())
A, B = a,b

while a != 0:
    b = b % a
    a, b = b, a
gcd = b
lcm = A * B // b
print(gcd)
print(lcm)


"""
a,b=map(int,input().split());l=a*b
while b:a,b=b,a%b
print(a,l//a)
"""