import sys
inStr, word = sys.stdin.read(), [0 for i in range(26)]

for s in inStr:
    if s.islower():
        word[ord(s)-97] += 1
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end='')




"""
from statistics import*
print(''.join(sorted(multimode(''.join(open(0).read().split())))))
"""