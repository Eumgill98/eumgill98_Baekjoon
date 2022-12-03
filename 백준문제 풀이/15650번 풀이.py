n, m = list(map(int, input().split()))

s = []
total = []

def dfs():
    if len(s) ==m and sorted(s) not in total:
        print(' '.join(map(str, s)))
        total.append(sorted(s))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
