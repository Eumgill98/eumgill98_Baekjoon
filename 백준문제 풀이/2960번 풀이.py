#에라토스테네스의 체
# 2부터 소수를 구하고자 하는 구간의 모든 수를 나열
## 자신인 2를 제외한 모든 2의 배수를 지움
### 다음 3이 소수이므로 소수에 3ㅜ가 그리고 3의 배수를 지움

"""
def getPrimaryNum_Eratos(N):
    nums = [True] * (N+1)
    for i in range(2, len(nums) // 2 +1):
        if nums[i] == True:
            for j in range(i+i, N, i):
                nums[j] = False
    return [ i for i in range(2, N) if nums=[i] == True]
"""


N, K = map(int, input().split())
cnt = 0
nums = [True] * (N+1)
for i in range(2, len(nums) + 1):
    for j in range(i, N+1, i):
        if nums[j] == True:
            nums[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break
