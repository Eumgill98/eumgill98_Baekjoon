total = []

while True:
    num = input()
    if num == '0':
        break
    while True:
        num_list = [int(f) for f in num]
        num = sum(num_list)
        num = str(num)
        if int(num) < 10:
            break
    total.append(num)

for i in total:
    print(i)



"""
while True:
    N = int(input())
    if N==0: quit()
    print((N+8)%9+1)
"""