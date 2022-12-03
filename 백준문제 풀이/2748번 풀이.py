num = int(input())
num_list =[0, 1]

for i in range(2, num+1):
    hab = num_list[i-2]+num_list[i-1]
    num_list.append(hab)

print(num_list[-1])

"""
a,b=0,1;exec("a,b=b,a+b;"*int(input()));print(a)
"""