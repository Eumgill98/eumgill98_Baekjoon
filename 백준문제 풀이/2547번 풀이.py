import sys

num = int(sys.stdin.readline())
input()
total_candy = []

for i in range(num):
    case = int(sys.stdin.readline())
    candy_list = []
    for _ in range(case):
        candy = int(sys.stdin.readline())
        candy_list.append(candy)
    if i == num-1 :
        pass
    else:
        input()
    total_candy.append(candy_list)


for i in range(num):
    if sum(total_candy[i]) % len(total_candy[i]) == 0:
        print('YES')
    else:
        print('NO')




"""
I=input
exec("I();N=int(I());print(['NO','YES'][sum(int(I()) for _ in [0]*N)%N==0]);"*int(I()))
"""