n,*l=map(int,open(0).read().split())
c=[0]*(10**5+3)
for i in l:
  for j in (-1,0,1): c[i+j]+=1
print(max(c))