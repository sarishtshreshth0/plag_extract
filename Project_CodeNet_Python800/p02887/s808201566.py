N=int(input())
S=input()
ans=0
p=''
for s in S:
    if s!=p:
        p=s
        ans+=1
print(ans)