maxa=10**10*(-1)
def euclid(a, b):
  if b == 0:
    return a
  else:
    return euclid(b, a%b)
N=int(input())
L=list(map(int,input().split()))
A=[0]*N
B=[0]*N
a=L[0]
A[0]=a
b=L[-1]
B[0]=b
for i in range(N-1):
  A[i+1]=euclid(A[i],L[i+1])
  B[i+1]=euclid(B[i],L[-(i+2)])
A.pop(-1)
B.pop(-1)
maxa=max(B[-1],A[-1])
for i in range(N-2):
  maxa=max(maxa,euclid(A[i],B[N-3-i]))
print(maxa)