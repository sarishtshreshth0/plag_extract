n=int(input())
s=input()
res=1
for i in range(1,len(s)):
    if s[i-1]!=s[i] :
        res+=1
print(res)