#이분탐색
import sys
input = sys.stdin.readline


def b_s(start, end, data, target):

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


T = int(input())
for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()

    M = int(input())
    M_list = list(map(int, input().split()))
    for i in M_list:
        print(b_s(0, N-1, N_list, i))


