num = int(input())
k = 0
total = 0
for i in range(num):
    error = 0
    word = input()


    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                error +=1
                break
    total +=error
    k+=1

print(k - total)