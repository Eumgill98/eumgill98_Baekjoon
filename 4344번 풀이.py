total =[]
for i in range(int(input())):
    class_room = [int(f) for f in input().split()]
    member = class_room[0]
    score = class_room[1:]
    class_median = sum(score) / member

    count = 0
    for i in score:
        if i > class_median:
            count +=1
    percentage = round((count / member) * 100, 3)
    total.append(percentage)


for i in total:
    print(f'{i:.3f}%')