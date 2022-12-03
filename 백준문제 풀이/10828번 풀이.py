import sys
total = []
for i in range(int(input())):
    key = str(sys.stdin.readline())
    if 'push' in key:
        num = int(key[5:])
        total.append(num)
    elif 'pop' in key:
        if total == []:
            print(-1)
        else:
            print(total[-1])
            total.pop()
    elif 'size' in key:
        print(len(total))
    elif 'empty' in key:
        if total ==[]:
            print(1)
        else :
            print(0)
    elif 'top' in key:
        if total ==[]:
            print(-1)
        else:
            print(total[-1])

