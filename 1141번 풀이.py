import sys

input = sys.stdin.readline

num = int(input())
santance = []
for _ in range(num):
    santance.append(input().rstrip())


santance.sort(key=len)
count = 0

for i in range(num):
    check = santance[i]
    pross = False
    for j in range(i+1, num):
        if check == santance[j][0:len(check)]:
            pross = True
            break

    if not pross:
        count +=1


print(count)