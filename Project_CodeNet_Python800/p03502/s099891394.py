n=input()
temp=0
for i in n:
  temp+=int(i)

print('Yes' if int(n)%temp==0 else 'No')