
for _ in range(int(input())):
    total = []
    mention = [f for f in input().split()]
    for i in range(len(mention)):
        stance = mention[i][::-1]
        total.append(stance)

    print(" ".join(total))
