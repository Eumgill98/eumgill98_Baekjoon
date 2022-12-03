num = int(input())
s = []

def make():
    if len(s) == num:
        print(' '.join(map(str, s)))
        return

    for i in range(1, num+1):
        if i not in s:
            s.append(i)
            make()
            s.pop()

make()