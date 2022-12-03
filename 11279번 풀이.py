import heapq
import sys

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    num = int(input())
    if num ==0  and heap ==[]:
        print(0)
    elif num == 0:
        result = (-heapq.heappop(heap))
        print(result)
    else:
        heapq.heappush(heap, -num)
