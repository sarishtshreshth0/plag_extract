s=input()
cnt1b,cnt2b,cnt1w,cnt2w=0,0,0,0
for i in range(len(s)):
  if i%2==0:
    if s[i]=='0':
      cnt1b+=1
    else:
      cnt1w+=1
  else:
    if s[i]=='0':
      cnt2b+=1
    else:
      cnt2w+=1
print(min(cnt1b+cnt2w,cnt2b+cnt1w))