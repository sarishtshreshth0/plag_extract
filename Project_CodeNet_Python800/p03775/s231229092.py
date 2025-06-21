import math
N=int(input())

ans=[]
is_prime = [True] * (int(N**(0.5))+1)
is_prime[0] = False
for i in range(1,int(N**(0.5))+1):
    if not is_prime:
        continue
    if N%i==0:
        ans.append([i,N//i])
    else:
        for j in range(i,int(N**(0.5))+1,i):
            is_prime[j]=False

z=10
for A in ans:
    z=min(z,int(math.log10(A[1])))

print(z+1)
