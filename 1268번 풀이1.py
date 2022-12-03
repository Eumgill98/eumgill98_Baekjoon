import sys

input = sys.stdin.readline

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * N
for n in range(N):
    visited = [False for _ in range(N)]
    for grade in range(5):
        for student_id in range(N):
            if student_id != n and data[student_id][grade] == data[n][grade]:
                visited[student_id] = True

    cnt[n] = len(list(filter(lambda x: x, visited)))

print(cnt.index(max(cnt)) + 1)