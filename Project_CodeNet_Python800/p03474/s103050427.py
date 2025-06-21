a,b = map(int, input().split())
s = input()
flg = 1
for i in range(len(s)):
    if i == a: continue
    elif '0' <= s[i] <= '9': flg = 1
    else: 
        flg = 0
        break

if (len(s) == a+b+1 and s[a] == '-' and flg) :print("Yes")
else: print("No")