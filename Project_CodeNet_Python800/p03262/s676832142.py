import fractions
N,X = map(int,input().split())

x = list(map(int,input().split()))
lst = [0]*N
for i in range(len(x)):
    lst[i] = x[i] - X
   
a=0
for e in lst:
  a=fractions.gcd(a,e)
print(abs(a))