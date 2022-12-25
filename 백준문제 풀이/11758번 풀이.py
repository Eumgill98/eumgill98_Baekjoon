#CCW 알고리즘

def ccw(a, b, c):
    return (a[0]*b[1]) + (b[0]*c[1]) + (c[0]*a[1]) - (b[0]*a[1] + c[0]*b[1] + a[0]*c[1])

total = []
for _ in range(3):
    a, b = map(int, input().split())
    total.append([a, b])

result = ccw(total[0], total[1], total[2])

if result >0 :
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)



