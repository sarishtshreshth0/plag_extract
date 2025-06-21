s=list(input())
n=len(s)
s1=["0"for i in range(n)]
s2=["1"for i in range(n)]
for i in range(0,n,2):
    s1[i]="1"
    s2[i]="0"
tmp1=0
tmp2=0
for i in range(n):
    if s[i]!=s1[i]:
        tmp1+=1
    if s[i]!=s2[i]:
        tmp2+=1
print(min(tmp1,tmp2))