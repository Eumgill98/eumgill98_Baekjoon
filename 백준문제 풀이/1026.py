num = int(input())
a = [int(f) for f in input().split()]
b = [int(k) for k in input().split()]



a = sorted(a)
n_b = sorted(b)[::-1]
product = [x*y for x,y in zip(a,n_b)]
print(sum(product))



