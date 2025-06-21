a, b = map(int, input().split())
s = input()
flag = 0
for i in range(a):
    if s[i]>='0' and s[i]<='9': pass
    else: flag=1
if s[a]!='-': flag=1
for i in range(a+1, len(s)):
    if s[i]>='0' and s[i]<='9': pass
    else: flag=1
if flag==1: print("No")
else: print("Yes")