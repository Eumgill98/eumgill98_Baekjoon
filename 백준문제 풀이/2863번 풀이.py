import sys
a,b = map(int, sys.stdin.readline().split())
c,d = map(int, sys.stdin.readline().split())
total = [a/c + b/d,c/d+a/b,d/b+c/a,b/a+d/c]
print(total.index(max(total)))


#수정
"""
a,b,c,d=map(int,open(0).read().split())
l=[a/c+b/d,c/d+a/b,d/b+c/a,b/a+d/c]
print(l.index(max(l)))
"""
