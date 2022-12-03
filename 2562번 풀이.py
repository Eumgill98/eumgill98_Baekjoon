import sys

num_list = []

for i in range(9):
    num = int(sys.stdin.readline())
    num_list.append(num)

print(max(num_list))
print(num_list.index(max(num_list))+1)



"""print(*max((int(input()),i+1)for i in range(9)))"""