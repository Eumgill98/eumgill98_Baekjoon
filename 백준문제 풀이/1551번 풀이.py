a, b = map(int, input().split())
origin = list(input().split(','))
new_list = []
if b==0:
    print(','.join(origin))

k=0
while k<b:
    if k >=1:
        origin=new_list
        new_list=[]
    for i in range(len(origin)-1):
        new_oneso = int(origin[i+1]) - int(origin[i])
        new_list.append(str(new_oneso))
    k+=1


print(','.join(new_list))