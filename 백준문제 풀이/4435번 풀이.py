battle = int(input())
gandal = [1, 2, 3, 3, 4 , 10]
saulon = [1 ,2, 2, 2, 3, 5, 10]
answer = []



for i in range(battle):
    g = [k for k in input().split()]
    s = [k for k in input().split()]
    g_total_list = []
    s_total_list = []

    for j in range(len(g)):
        g_total = int(g[j])*gandal[j]
        g_total_list.append(g_total)

    for j in range(len(s)):
        s_total = int(s[j])*saulon[j]
        s_total_list.append(s_total)

    if sum(g_total_list) < sum(s_total_list):
        an = f"Battle {i+1}: Evil eradicates all trace of Good"
    elif sum(g_total_list) > sum(s_total_list):
        an =f"Battle {i+1}: Good triumphs over Evil"
    else :
        an = f"Battle {i+1}: No victor on this battle field"
    answer.append(an)

for i in range(len(answer)):
    print(answer[i])




"""
f=lambda x:sum(map(lambda a:a[0]*a[1],zip(x,map(int,input().split()))))
g=[1,2,3,3,4,10]
s=[1,2,2,2,3,5,10]
for i in range(int(input())):G=f(g);S=f(s);print(f"Battle {i+1}: {[['Evil eradicates all trace of Good','No victor on this battle field'][G==S],'Good triumphs over Evil'][G>S]}")
"""




