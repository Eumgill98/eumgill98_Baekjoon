student = int(input())
wanted = [int(f) for f in input().split()]
wanted.sort()
count = 0
i = 0
while True:
    if i == len(wanted):
        break

    if wanted[i] == 1:
        count +=1
        i+=1
    elif wanted[i] > 1:
        if (i + wanted[i]) > len(wanted):
            i = len(wanted)
            count += 1
        else:
            i += (wanted[i])
            count += 1

print(count)