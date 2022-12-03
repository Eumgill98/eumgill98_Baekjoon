import sys
total = []

while True:
    o, w = map(int, sys.stdin.readline().split())
    if o == 0 and w ==0:
        break
    while True:
        bh, n = map(str, sys.stdin.readline().split())
        if bh == '#' and n == '0':
            break
        if w <=0:
            pass
        else:
            if bh == 'E':
                w -= int(n)
            else:
                w += int(n)

    if w > (0.5*o) and w < (2*o):
        emotion = ':-)'
    elif w <=0:
        emotion = 'RIP'
    else:
        emotion = ':-('
    total.append(emotion)


for i in range(len(total)):
    print((i+1), total[i])
