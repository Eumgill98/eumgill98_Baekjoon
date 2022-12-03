num = int(input())
tall = list(map(int, input().split()))
reslut = [0 for  f in range(num)]

for i in range(num):
    cnt = 0
    for j in range(num):
        if cnt == tall[i] and reslut[j] == 0:
            reslut[j] = i+1
            break
        elif reslut[j] == 0:
            cnt += 1

print(*reslut)

