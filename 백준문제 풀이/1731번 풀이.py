num = int(input())
total =[]
for i in range(num):
    total.append(int(input()))

if total[2]-total[1] == total[1]-total[0]:
    print(total[-1]+(total[1]-total[0]))
else:
    print(total[-1]*(total[1]//total[0]))
