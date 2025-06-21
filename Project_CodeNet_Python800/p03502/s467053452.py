n=int(input())
m=list(str(n))
res=0
for i in m:res+=int(i)
print("Yes" if n % res == 0 else "No")
