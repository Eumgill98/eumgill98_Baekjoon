import sys
input = sys.stdin.readline

n, k = map(int, input().split())
HP = list(f for f in input())
count = 0
for i in range(n):
    if HP[i] == 'P':
        for j in range(max(i-k,0), min(i+k+1, n)):
            if HP[j] == 'H':
                HP[j] = '0'
                count +=1
                break
print(count)