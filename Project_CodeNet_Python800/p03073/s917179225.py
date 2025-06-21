cnt=0
cnt_2=0
s = str(input())
for i in range(len(s)):
    if s[i]=='0' and i%2==0:
        cnt+=1
    if s[i]=='1' and i%2==0:
        cnt_2+=1
    if s[i]=='1' and i%2!=0:
        cnt+=1
    if s[i]=='0' and i%2!=0:
        cnt_2+=1
print(min(cnt,cnt_2))