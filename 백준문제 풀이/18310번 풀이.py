n = int(input())
house = [int(f) for f in input().split()]
house.sort()


print(house[(n-1)//2])