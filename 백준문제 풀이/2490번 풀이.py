answer = []

for i in range(3):
    mal = [j for j in input().split(" ")]
    if mal.count('0') == 0:
        num = 'E'
    elif mal.count('0') == 1:
        num = 'A'
    elif mal.count('0') == 2:
        num = 'B'
    elif mal.count('0') == 3:
        num = 'C'
    elif mal.count('0') == 4:
        num = 'D'
    answer.append(num)

for a in answer:
    print(a)



""" 
숏코딩 1
exec("print('EABCD'[input().count('0')]);"*3)
"""

"""
숏코딩 2
for _ in [0]*3:print("DCBAE"[input().count("1")])
"""
