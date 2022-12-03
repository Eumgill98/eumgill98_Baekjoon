num_list = []

for _ in range(int(input())):
    mention = int(input())
    if mention ==0:
        num_list.pop(-1)
    else:
        num_list.append(mention)

print(sum(num_list))