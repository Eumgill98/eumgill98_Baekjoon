import sys
input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    s_list = list(map(str, input().split()))
    point = [s_list.pop(0)]
    for i in s_list:
        if point[0] >= i:
            point.insert(0, i)
        else:
            point.append(i)

    print("".join(point))



