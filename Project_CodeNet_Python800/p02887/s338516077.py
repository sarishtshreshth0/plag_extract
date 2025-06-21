input()
S=input()

while True:
 x=''
 ans=''
 for i in S:
   if (x==''):
    x=i
    continue
   if x!=i:
    ans+=x
    x=i
 ans+=x
 if ans==S:
   break
 else:
   S=ans
print(len(ans))       