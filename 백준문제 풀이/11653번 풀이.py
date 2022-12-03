X = int(input())
while X !=1:
    for i in range(2, X+1):
        if X % i == 0:
            print(i)
            count = i
            break
    X = X//count