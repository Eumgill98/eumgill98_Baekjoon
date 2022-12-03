hack_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

string = input()
for i in hack_list:
    if i in string :
        while True:
            count+=1
            string = string.replace(i, '0', 1)
            if i not in string:
                break

for j in string:
    if j == '0':
        pass
    else:
        count+=1

print(count)




