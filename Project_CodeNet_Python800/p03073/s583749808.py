s=input()
ans1=''
ans2=''
for i in range(len(s)):
    if i%2==0:
        ans1+='1'
        ans2+='0'
    else:
        ans1+='0'
        ans2+='1'
tmp1=0
tmp2=0
for i in range(len(s)):
    if s[i]!=ans1[i]:
        tmp1+=1
    if s[i]!=ans2[i]:
        tmp2+=1
print(min(tmp1,tmp2))