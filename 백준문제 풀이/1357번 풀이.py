a, b = map(str, input().split())
def rev(num):
    num = int(num[::-1])
    return num

print(int(str((rev(a)+rev(b)))[::-1]))
