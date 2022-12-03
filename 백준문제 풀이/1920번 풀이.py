#이분 탐색문제
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

A.sort()

#arr의 각 원소별 이분탐색
for num in arr:
    start, end = 0, N - 1
    Exist = False

    #이분탐색시작
    while start <= end:
        mid = (start + end) // 2
        if num == A[mid]:
            Exist =True
            print(1)
            break
        elif num > A[mid]:
            start = mid + 1
        else:
            end = mid -1

    if not Exist:
        print(0)



"""
# 입력
N = int(input())
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for num in arr:				# arr의 각 원소별로 탐색
    print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력"""