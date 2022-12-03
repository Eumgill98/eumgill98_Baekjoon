import sys

for i in range(int(sys.stdin.readline())):
    floor = int(sys.stdin.readline())
    room = int(sys.stdin.readline())

    floor_0 =[]
    for k in range(1, room+1):
        people = k
        floor_0.append(k)

    total_floor =[]
    total_floor.append(floor_0)
    for j in range(1, floor+1):
        j_floor = []
        for f in range(1, room+1):
            ra = total_floor[j-1][:f]
            j_floor.append(sum(ra))
        total_floor.append(j_floor)
    print(total_floor[-1][-1])
