#정렬 문제
import sys
input = sys.stdin.readline

work = int(input())
total = []
for _ in range(work):
    start, end = map(int, input().split())
    total.append([start, end])


total.sort(key=lambda x: x[0])
total.sort(key=lambda x: x[1])


ing = 0
cnt = 0

for i, j in total:
    if i >= ing:
        cnt += 1
        ing = j

print(cnt)