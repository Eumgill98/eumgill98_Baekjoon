name = input()
names = [0] * 26

for j in name:
    names[ord(j) - 65] += 1

a = 0
a_a = ""
a_c = ""

for i in range(26):
    if names[i] % 2 == 1:
        a += 1
        a_a += chr(i + 65)
    a_c += chr(i+65) * (names[i] // 2)

if a > 1:
    print("I'm Sorry Hansoo")
else:
    print(a_c + a_a + a_c[::-1])
