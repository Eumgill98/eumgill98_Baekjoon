def d(n):
    num = int(n)
    for i in str(n):
        num += int(i)
    return num

non_self = []
for i in range(1, 10001):
    num = d(i)
    non_self.append(num)

for j in range(1, 10001):
    if j not in non_self:
        print(j)
