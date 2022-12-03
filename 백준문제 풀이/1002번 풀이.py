import sys
input= sys.stdin.readline()

num = int(input)
for _ in range(num):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())

    if r1 > r2:
        x_temp = x1
        y_temp = y1
        r_temp = r1
        x1, y1, r1  = x2, y2, r2
        x2, y2, r2 = x_temp, y_temp, r_temp

    pythagoras = ((x2-x1)**2 + (y2-y1)**2)**0.5
    radius = r1 + r2

    if x1 == x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
    elif pythagoras > radius or pythagoras+r1 < r2:
        print(0)
    elif pythagoras == radius or pythagoras+r1 == r2:
        print(1)
    elif r2-r1 < pythagoras < radius:
        print(2)