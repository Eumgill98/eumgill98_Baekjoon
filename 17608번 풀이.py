import sys
input = sys.stdin.readline
total =[]
for i in range(int(input())):
    total.append(int(input()))

point = total.pop()
result = [point]

for _ in range(len(total)):
    delet = total.pop()
    if delet > point:
        point = delet
        result.append(point)

    else:
        pass

print(len(result))