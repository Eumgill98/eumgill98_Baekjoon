from itertools import combinations


while True:
    mention = [int(f) for f in input().split()]
    if mention == [0]:
        break
    del mention[0]
    s= list(combinations(mention,6))
    for i in s:
        for j in i:
            print(j, end=" ")
        print()
    print()



"""" 다른 풀이
#dfs를 활용한 풀이
def dfs(depth, idx):
    if depth == 6:
    print(*out)
    return 
    
    for i in range(idx, k):
        out.append(S[i])
        dfs(depth +1, i+1)
        out.pop()
        
while True:
    array = list(map(int, input().split())
    k = array[0]
    S = array[1:]
    out = []
    dfs(0,0)
    if k == 0:
        exit()
    print()

"""