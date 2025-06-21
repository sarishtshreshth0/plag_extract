from copy import deepcopy
s=list(map(int,input()))
t=deepcopy(s)
if t[0]==1:
    t[0]=0
else:
    t[0]=1

cnt=0
rev_cnt=1

for i in range(1,len(s)):
    if s[i-1]==s[i]:
        if s[i]==0:
            s[i]=1
        else:
            s[i]=0
        cnt+=1

for i in range(1,len(t)):
    if t[i-1]==t[i]:
        if t[i]==0:
            t[i]=1
        else:
            t[i]=0
        rev_cnt+=1

print(min(cnt, rev_cnt))