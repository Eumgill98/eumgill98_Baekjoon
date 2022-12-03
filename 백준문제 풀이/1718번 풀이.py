from string import ascii_lowercase
import sys

input = sys.stdin.readline

alphabet_list = list(ascii_lowercase)

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

x = input()
y = input()

input_list = []
compare_list = []

for i in x:
    if i == '\n':
        pass
    else :
        input_list.append(i)

for j in y:
    if j == '\n':
        pass
    else:
        compare_list.append(j)


input_list = list_chunk(input_list, len(compare_list))

answer = []

for a in range(len(input_list)):
    for b in range(len(compare_list)):
        if input_list[a][b] == ' ':
            stance = ' '
        else:
            key = alphabet_list.index(input_list[a][b]) - alphabet_list.index(compare_list[b])-1

            if key < 0:
                key + 25
            stance = alphabet_list[key]
        answer.append(stance)


print(''.join(answer))






### 다른 풀이
text, key = input(), input()

answer = ''

for i in range(len(text)):
    if text[i] == ' ': answer += ' '
    else: answer += chr((ord(text[i]) - ord(key[i%len(key)]) - 1) % 26 + ord('a'))

print(answer)