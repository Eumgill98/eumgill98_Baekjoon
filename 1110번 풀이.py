num = input()

if int(num)<10:
    num = '0'+num

origin_num = num
cnt = 0
while True:
    if int(num[0])+int(num[1])>=10:
        k = str(int(num[0])+int(num[1]))
        num = num[1]+k[1]
    else:
        num = num[1]+str(int(num[0])+int(num[1]))
    cnt +=1
    if num == origin_num:
        break

print(cnt)