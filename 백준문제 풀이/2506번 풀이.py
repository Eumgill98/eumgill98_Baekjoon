import sys

k=1
total = 0
numclass = int(sys.stdin.readline())
ox_list = [int(f) for f in sys.stdin.readline().split()]

for i in range(len(ox_list)):
    if ox_list[i]==0:
        k=0
        num = ox_list[i] * k
        k+=1
    else:
        num = ox_list[i] * k
        k+=1
    total+=num

print(total)