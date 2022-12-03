import sys

num = int(sys.stdin.readline())

score = [int(f) for f in sys.stdin.readline().split()]

new_score = []
for i in range(len(score)):
    new = int(score[i])/max(score)*100
    new_score.append(new)

print(sum(new_score)/num)