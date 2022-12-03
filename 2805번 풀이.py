import sys
input = sys.stdin.readline

def binary_search(arr, start, end):
    res = 0
    while start <= end:
        mid = (start+end) // 2
        total = 0

        for x in arr:
            if x > mid:
                total+= x - mid
        if total < m:
            end = mid - 1
        else:
            res = mid
            start = mid +1
    return res

n, m = map(int, input().split())
trees = list(map(int,input().split()))

r = binary_search(trees, 0, max(trees))

print(r)