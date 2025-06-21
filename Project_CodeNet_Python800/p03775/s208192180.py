n,r=int(input()),1e9
for i in range(1,int(n**.5)+1):
  if n%i==0: r=min(r,max(len(str(i)),len(str(n//i))))
print(r)