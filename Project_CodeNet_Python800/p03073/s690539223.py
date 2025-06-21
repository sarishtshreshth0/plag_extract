s=list(input())
s=[int(s[i]) for i in range(len(s))]
tile=s[0]
cnt=0
for i in range(1,len(s)):
    if s[i]==tile:
        cnt+=1
    if tile==1:
        tile=0
    else:
        tile=1
print(cnt)