
import itertools

N, S = map(int, input().split())
array = list(map(int, input().split()))
count = 0

for i in range(1, N + 1):
    for j in itertools.combinations(array, i):
        if sum(j) == S:
            count += 1

print(count)




### combinations를 함수로 구현
def combinations(arr, n):
    result = []

    if n ==0:
        return[[]]
    for i in range(0, len(arr)):
        ele = arr[i]
        start_arr = arr[i+1 :]
        for c in combinations(start_arr, n-1):
            result.append([ele]+c)

        return result
