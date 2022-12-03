def sosu_find(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

num_len = int(input())
num_list =[int(f) for f in input().split()]

k = 0
for j in num_list:
    if j ==1 :
        pass
    elif sosu_find(j) == True:
        k+=1
    else:
        pass

print(k)