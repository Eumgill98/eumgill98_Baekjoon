num = int(input())

while True:
    boll = True
    for i in str(num):
        if i!='4' and i!='7':
            boll = False
            num -=1

    if boll:
        print(num)
        break
