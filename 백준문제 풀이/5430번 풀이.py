import sys
from collections import deque

input = sys.stdin.readline

case = int(input())

for i in range(case):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    q = deque(arr)

    r,f,b = 0, 0, len(q)-1
    flag = True
    if n ==0:
        q=[]
        f=0
        back=0

    for j in p:
        if j =='R':
            r +=1
        elif j =='D':
            if len(q) < 1:
                flag=False
                print('error')
                break
            else:
                if r % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag == True:
        if r % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
