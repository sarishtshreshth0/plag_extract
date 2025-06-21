N=input()
n=int(N)
N=list(N)
check=0
for i in range(0,len(N)):
  check+=int(N[i])
print("Yes" if n%check==0 else "No")
