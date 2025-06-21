n=int(input())
a=[0 for i in range(n)]
for i in range(n-1):
    c,s,f=map(int,input().split())
    for j in range(i+1):
        a[j]=-max(a[j],s)//f*-f+c
print(*a,sep='\n')