import sys
day_30 =[4, 6, 9, 11]
day_31 = [1,3,5,7,8,10,12]

while True:
    #날짜 카운트 변수 초기화
    count = 0
    #인풋값
    day, month, year = map(int, sys.stdin.readline().split())
    #종료코드
    if day==0 and month==0 and year==0:
        break

    #해당달을 제외한 날짜 카운트
    for i in range(1, month):
        if i in day_30:
            count += 30
        elif i in day_31:
            count += 31
        elif i ==2:
            if (year%4==0 and year%100 !=0) or year%400==0:
                count +=29
            else:
                count +=28


    count += day
    print(count)

