s=input()
a=0
for i in range(len(s)):
  a+=int(s[i])
print('Yes' if int(s)%a==0 else 'No')