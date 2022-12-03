import sys
input = sys.stdin.readline

for i in range(int(input())):
    string = list(map(str, input().split()))
    string = string[::-1]

    print(f'Case #{i+1}: '+" ".join(string))