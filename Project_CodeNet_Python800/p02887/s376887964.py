input()
S=input()

l=S[0]
c=1
for i in S[1:]:
 if l!=i:
  c+=1
  l=i
print(c)