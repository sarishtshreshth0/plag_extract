s=[]
S=input()
for i in S:
    s+=[int(i)]
#print(s)
ans=0
if s[0]==0:
    for i in s[0::2]:
        if i!=0:
            ans+=1
            #print(0,i,ans)
    for i in s[1::2]:
        if i!=1:
            ans+=1
            #print(1,i,ans)
#print(s[0::2],s[1::2])
if s[0]==1:
    for i in s[0::2]:
        if i!=1:
            ans+=1
    for i in s[1::2]:
        if i!=0:
            ans+=1
print(ans)