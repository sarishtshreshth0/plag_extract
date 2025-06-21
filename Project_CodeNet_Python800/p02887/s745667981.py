n=int(input())
s=list(input())
cnt=0
for i in range(0,n-1):
    if s[i]==s[i+1]:
        continue
    else:
        cnt+=1
print(cnt+1)