n, m = list(map(int, input().split()))
s = []
total = []
n_list = sorted([int(f) for f in input().split()])

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in n_list:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()