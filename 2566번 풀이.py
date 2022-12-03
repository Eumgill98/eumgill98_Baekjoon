import sys
df = []

for i in range(9):
    num_list = [int(i) for i in sys.stdin.readline().split()]
    df.append(num_list)

max_list = sum(df, [])
max_num = max(max_list)
h = ((max_list.index(max_num)//9)+1)
y = ((max_list.index(max_num)-((h-1)*9))+1)
print(max_num)
print(h, y)

