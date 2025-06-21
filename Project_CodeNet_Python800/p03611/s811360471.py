n=int(input())
l=list(map(int,input().split()))
d=[0]*(10**5+1)
for i in l:
   d[i]+=1
s=list(set(l))
m=len(s)
k=0
for i in range(m):
    k=max(d[s[i]-1]+d[s[i]]+d[s[i]+1],k)
print(k)
