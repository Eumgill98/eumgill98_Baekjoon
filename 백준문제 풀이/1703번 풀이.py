import sys
total = []
while True:
    leaf = 1
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(li[0]):
        leaf = (leaf *  li[(2*i)+1]) - li[(2*i)+2]

    if li == [0]:
        pass
        break
    else :
        total.append(leaf)

for i in total:
    print(i)



"""
*z,_=open(0)
for l in z:
 n,*x=map(int,l.split());a=1
 for i in range(n):a=a*x[i+i]-x[i-~i]
 print(a)
"""

