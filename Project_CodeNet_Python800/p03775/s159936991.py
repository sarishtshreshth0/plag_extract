
import math
N=int(input())

def func(A,B):
  if A > B:
    return len(str(A))
  else:
    return len(str(B))


ans=[]
N2=math.floor(math.sqrt(N))
for A in range(1,N2+1):
  if N%A==0:
    B=int(N/A)
    ans.append(func(A,B))

print(min(ans))