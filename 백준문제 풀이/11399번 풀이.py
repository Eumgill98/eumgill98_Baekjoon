human = int(input())
time_list = [0]*human
use_time = [int(f) for f in input().split()]
use_time = sorted(use_time)

for i in range(human):
    if i ==0:
        time_list[i] =use_time[i]
    else:
        time_list[i] = use_time[i]+ time_list[i-1]

print(sum(time_list))