import sys

for i in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    if b == 'kg':
        print("%.4f lb" % (float(a) * 2.2046))
    elif b == 'l':
        print("%.4f g" % (float(a) * 0.2642))
    elif b == 'lb':
        print("%.4f kg" % (float(a) * 0.4536))
    elif b == 'g':
        print("%.4f l" % (float(a) * 3.7854))