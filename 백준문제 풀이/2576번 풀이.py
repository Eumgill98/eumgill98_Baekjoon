import sys
num_list = []
total_list = []

for i in range(7):
    num = int(sys.stdin.readline())
    if num % 2 == 1:
        num_list.append(num)


num_list = sorted(num_list)
if num_list ==[]:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])
