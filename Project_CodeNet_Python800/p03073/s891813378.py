s=list(input())
a=["0","1"]
cnt=0
for i in range(len(s)):
    if s[i]!=a[i%2]:
        cnt+=1
print(min(cnt,len(s)-cnt))