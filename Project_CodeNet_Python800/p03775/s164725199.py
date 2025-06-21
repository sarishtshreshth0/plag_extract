n,r=int(input()),1e9
print(min([len(str(n//i)) for i in range(1,int(n**.5)+1) if n%i==0]))