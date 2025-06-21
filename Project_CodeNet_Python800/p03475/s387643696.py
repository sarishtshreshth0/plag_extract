N=int(input())
L=[]
for i in range(N-1):
    c,s,f=map(int, input().split())
    L.append((c,s,f))

for i in range(N):
    if i==N-1:
        print(0)
    now=0
    for j in range(i,N-1):
        c,s,f=L[j]
        if now<s:
            now+=s-now
        if now%f!=0:
            now+=(f-now%f)
        now+=c
        if j==N-2:
            print(now)
