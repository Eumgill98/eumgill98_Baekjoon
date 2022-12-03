a_list = []

for i in range(3):
    a = input()
    a_list.append(a)

if a_list[1] == "*":
    calculate = int(a_list[0])*int(a_list[2])
else:
    calculate = int(a_list[0])+int(a_list[2])

print(calculate)

"""
i=input
print(eval(i()+i()+i()))
숏코딩
"""