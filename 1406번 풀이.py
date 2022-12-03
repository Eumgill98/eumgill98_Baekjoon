"""import sys
input = sys.stdin.readline

main = list(input().strip())
num = int(input())
index = len(main)

for _ in range(num):
    command = list(input().split())
    if command[0] =='P':
        main.insert(index, command[1])
        index += 1
    elif command[0] == 'L':
        if index > 0:
            index -= 1
    elif command[0] == 'D':
        if index < len(main):
            index += 1

    else:
        if index > 0:
            main.remove(main[index-1])

print("".join(main))
"""
#시간 초과
## How to 풀이 ?


import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())

    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()

    else:
        st1.append(command[1])

st1.extend(reversed(st2))
print(''.join(st1))
