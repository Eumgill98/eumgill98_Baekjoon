num = int(input())

for _ in range(num):
    n,m = list(map(int, input().split()))
    importance = list(map(int, input().split()))
    idx = list (range(len(importance)))
    idx[m] = 'know'

    count = 0

    while True:
        if importance[0] == max(importance):
            count +=1

            if idx[0] == 'know':
                print(count)
                break
            else:
                importance.pop(0)
                idx.pop(0)
        else:
            importance.append(importance.pop(0))
            idx.append(idx.pop(0))