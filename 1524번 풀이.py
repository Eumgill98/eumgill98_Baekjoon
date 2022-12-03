result=[]
for i in range(int(input())):
    input()
    n,m = map(int, input().split())
    n_stat = sorted([int(f) for f in input().split()])
    m_stat = sorted([int(f) for f in input().split()])



    while True:
        if n_stat==[] or m_stat==[]:
            break
        if n_stat[0]> m_stat[0]:
            m_stat.pop(0)
        elif n_stat[0]<m_stat[0]:
            n_stat.pop(0)
        elif n_stat[0]==m_stat[0]:
            m_stat.pop(0)

    if len(n_stat)<len(m_stat):
        result.append('B')
    elif len(n_stat)>len(m_stat):
        result.append('S')
    else:
        result.append('C')

for i in result:
    print(i)




"""
for _ in range(int(input())):input();input();print(['S','B'][max(map(int,input().split()))<max(map(int,input().split()))])
"""