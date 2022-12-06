def binary():
    start = 1
    end = max(n_list)
    while start <= end:
        mid = (start+end) //2
        money = 0
        for i in n_list:
            if i <= mid:
                money += i
            else:
                money += mid

        if money > m:
            end = mid - 1
        else:
            start = mid + 1

    return end

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
n_list.sort()

print(binary())
