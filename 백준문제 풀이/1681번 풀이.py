n, l = map(int, input().split())
total = []
k=0
while True:
    k +=1
    if str(l) in str(k):
        pass
    else:
        total.append(k)
    if len(total)==n:
        break

print(max(total))


