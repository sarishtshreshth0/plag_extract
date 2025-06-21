N=int(input())

def f(a,b):
  return max(len(str(a)), len(str(b)))

i=1
ans=float("inf")
while i**2<=N:
  if N%i==0:
    temp=f(i, N//i)
    ans=min(ans, temp)
  i+=1
print(ans)