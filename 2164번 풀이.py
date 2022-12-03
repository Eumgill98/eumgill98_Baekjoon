num = int(input())
s = 2

while True:
    if num == 1 or num ==2:
        print(num)
        break
    s *= 2
    if (s >= num):
        print((num - (s //2)) * 2)
        break