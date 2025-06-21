n=int(input())
f=0
frag='No'
for i in range(8):
  f+=n%(10**(i+1))//10**i
if n%f==0:
  frag='Yes'
print(frag)