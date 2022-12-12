import sys
input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(input().split()))

num_list = []

def dfs(x, y, num):
    if len(num) == 6:
        if num not in num_list:
            num_list.append(num)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx<0 or nx>=5 or ny<0 or ny >=5:
            continue
        else:
            dfs(nx, ny, num+board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(num_list))