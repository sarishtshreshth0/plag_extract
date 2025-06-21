n=int(input())
s=list(input())
c=0
out=0
for i in range(0,n-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        out+=c
        c=0
out+=c
out=n-out
print(out)