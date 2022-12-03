a_list = []
for i in range(5):
    a = input()
    a_list.append(a)

total_list = []
for k in range(len(a_list)):
    if 'FBI' in a_list[k]:
        total_list.append(k+1)

total_list = ' '.join(str(s) for s in total_list)

if total_list =='' :
    print('HE GOT AWAY!')
else:
    print(total_list)



""" 숏코딩 
if not[print(i)for i in range(1,6)if'FBI'in input()]:print('HE GOT AWAY!')
"""