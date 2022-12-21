
def make_code(cnt, idx):
    if cnt == l:
        vo, co = 0, 0

        for i in range(l):
            if answer[i] in vowel:
                vo += 1
            else:
                co += 1

        if vo >= 1 and co >= 2:
            print("".join(answer))
        return

    for i in range(idx, c):
        answer.append(c_list[i])
        make_code(cnt + 1, i + 1)
        answer.pop()


l, c = map(int, input().split())
c_list = [f for f in input().split()]
c_list.sort()
vowel = 'aeiou'
answer =[]
make_code(0, 0)