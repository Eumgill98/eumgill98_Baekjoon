import sys

num = sys.stdin.readline()
k = 0
for i in range(1, int(num)+1):
    if len(str(i)) <=2:
        k+=1

    elif len(str(i)) == 3 and (int(str(i)[1])-int(str(i)[0]) == int(str(i)[2])-int(str(i)[1])):
        k+=1

    elif len(str(i)) == 4 and (int(str(i)[1])-int(str(i)[0]) == int(str(i)[2])-int(str(i)[1])==int(str(i)[3])-int(str(i)[2])):
        k+=1

print(k)