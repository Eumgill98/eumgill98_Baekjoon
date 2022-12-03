n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]


result = []
num = 0 ##제거될 사람의 인덱스 번호

for j in range(n):
    num += k-1
    if num >= len(arr):
        num = num%len(arr)

    result.append(str(arr.pop(num)))

print("<",", ".join(result)[:],">", sep='')