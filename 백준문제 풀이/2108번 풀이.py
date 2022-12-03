import sys
from collections import Counter
input = sys.stdin.readline

def make_count(num):
    num = sorted(num)
    print(int(round(sum(num)/len(num),0)))
    print(num[len(num)//2])

    f = Counter(num)
    b = f.most_common()
    if len(num) > 1 :
        if b[0][1] == b[1][1]:
            print(b[1][0])
        else:
            print(b[0][0])
    else:
        print(num[0])
    print(max(num) - min(num))


num =[]
for i in range(int(input())):
    n = int(input())
    num.append(n)


make_count(num)




