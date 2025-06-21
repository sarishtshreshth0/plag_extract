n=int(input())
a=list(map(int,input().split()))

l=[0 for i in range(10**5+2)]

for i in range(n):
    l[a[i]-1]+=1
    l[a[i]]+=1
    l[a[i]+1]+=1
print(max(l))