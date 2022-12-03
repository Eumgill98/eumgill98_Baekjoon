n = int(input())
day = []
money = []

dp = [0]  * (n + 1)
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    day.append(x)
    money.append(y)

for i in range(n-1, -1, -1):
    time = day[i] + i
    if time <=n:
        dp[i] = max(money[i] + dp[time], max_value)
        max_value = dp[i]
        print('-'*40, 'if time <=n')
        print('i:',i)
        print('time', time)
        print('dp:', dp)
        print('max_value:', max_value)

    else:
        dp[i] = max_value
        print('-'*40, 'else')
        print('i:',i)
        print('time', time)
        print('dp:', dp)
        print('max_value:',max_value)
print(max_value)




"""
다른 풀이 방법  백트레킹
# 퇴사
N = int(input())
schedule_list = [list(map(int, input().split())) for _ in range(N)]

# 백트레킹으로 풀어야할 거같은데
max_sum = 0
def dfs(sum, day):
    global max_sum
    if max_sum <= sum:
        max_sum = sum
    # if day == N:  이 조건은 사용하지 않음
  
    for i in range(day, N):
        tmp = i + schedule_list[i][0] # 다음회차에 가능한지 체크
        if i + schedule_list[i][0] <= N: 
            dfs(sum + schedule_list[i][1] , i + schedule_list[i][0])
        
dfs(0,0)
print(max_sum)
"""