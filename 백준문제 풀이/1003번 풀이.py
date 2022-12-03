"""
cnt_0 = 0
cnt_1 = 0
def fibonacci(n):
    global cnt_0
    global cnt_1
    if n==0:
        cnt_0 +=1
        return 0
    elif n==1:
        cnt_1 +=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(int(input())):
    n = int(input())
    fibonacci(n)
    print(cnt_0, cnt_1)
    cnt_0=0
    cnt_1=0
"""

z = [1, 0, 1]
o = [0, 1, 1]

def new_fibona(n):
    length= len(z)
    if n>=length:
        for i in range(length, n+1):
            z.append(z[i-1] + z[i-2])
            o.append(o[i-1] + o[i-2])
    print(z[n], o[n])

for _ in range(int(input())):
    new_fibona(int(input()))
