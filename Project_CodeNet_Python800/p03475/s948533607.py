n=int(input())
lst=[]
for i in range(n-1):
    c,s,f=map(int,input().split())
    lst.append([c,s,f])

for i in range(n-1):
    time=0
    for j in range(i,n-1):
        if time<=lst[j][1]:
            time=lst[j][1]+lst[j][0]
            continue
        if time%lst[j][2]==0:
            time+=lst[j][0]
            continue
        time+=(lst[j][2]-time%lst[j][2])+lst[j][0]
    print(time)
print(0)