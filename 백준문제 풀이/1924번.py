day_31 = [1,3,5,7,8,10,12]
day_30 = [4,6,9,11]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU','FRI','SAT' ]

a,b = map(int, input().split())

day = 0
for i in range(1, a):
    if i in day_31:
        day+=31
    elif i in day_30:
        day+=30
    else:
        day+=28
day += b

print(days[day%7])
