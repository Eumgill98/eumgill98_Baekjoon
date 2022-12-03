import sys
from collections import Counter
s1, s2, s3 = map(int, sys.stdin.readline().split())

new_s1 = [f for f in range(1, s1+1)]
new_s2 = [f for f in range(1, s2+1)]
new_s3 = [f for f in range(1, s3+1)]

total = []
for i in new_s1:
    for j in new_s2:
        for k in new_s3:
            s_sum = sum([i,j,k])
            total.append(s_sum)

cnt = Counter(total)
model = cnt.most_common()
print(model[0][0])