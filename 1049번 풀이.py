n , m = map(int, input().split())
a=[]
b=[]
brand = []
for _ in range(m):
    six, one = map(int, input().split())
    a.append(six)
    b.append(one)

brand.append(min(a))
brand.append(min(b))

six= brand[0]
one = brand[1]

min_money = min((n//6)*six + (n%6)*one, (n//6 + 1)*six, n*one)

print(min_money)


