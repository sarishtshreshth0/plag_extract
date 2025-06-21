from collections import Counter
n=int(input())
a=list(map(int,input().split()))
ans=0
accum = [0]*(n+1)
accum[0]=0
for i in range(n):
    accum[i+1]=a[i]+accum[i]

z=Counter(accum)
for k,v in z.items():
    ans+=v*(v-1)/2
    
print(int(ans))
