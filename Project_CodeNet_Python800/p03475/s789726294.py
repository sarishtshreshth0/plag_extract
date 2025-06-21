n=int(input())
CSF=[list(map(int,input().split())) for _ in range(n-1)]

for i in range(n-1):
    time=0
    for j in range(i,n-1):
        c,s,f=CSF[j]
        if i==j:
            time +=c+s
            continue
        else:
            if time<s:time=s
            elif time%f!=0:time +=f-(time%f)
            time +=c
    print(time)
print(0)