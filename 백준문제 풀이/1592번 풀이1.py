N, M, L = map(int, input().split())
k_list = [0]*N
cnt = i = 0
while k_list[i] < M-1:
    k_list[i] += 1
    cnt += 1
    i = (i+L)%N if k_list[i]%2 == 1 else (i-L)%N
print(cnt)