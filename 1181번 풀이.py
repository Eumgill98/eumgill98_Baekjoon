total = []
for _ in range(int(input())):
    total.append(input())

#중복값 제거
set_total = list(set(total))

len_total = []
for i in set_total:
    len_total.append((len(i),i))

len_total = sorted(len_total)
for a,b in len_total:
    print(b)


