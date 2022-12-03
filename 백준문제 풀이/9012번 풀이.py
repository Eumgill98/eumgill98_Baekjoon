import sys

for _ in range(int(input())):
    string = sys.stdin.readline()
    count = 0
    for j in string:
        if j == '(':
            count+=1
        elif j == ')':
            count-=1

        if count < 0:
            break

    if count != 0:
        result ='NO'
    else:
        result ='YES'

    print(result)
