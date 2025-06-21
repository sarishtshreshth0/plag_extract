N = int(input())
A = list(map(int,input().split()))

from math import gcd
L=[A[0]]*N
R=[A[-1]]*N

for a_idx in range(1,len(A)):
    L[a_idx]=gcd(L[a_idx-1],A[a_idx])
    R[len(A)-a_idx-1]=gcd(R[len(A)-a_idx],A[len(A)-a_idx-1])

ans_list=[0]*N
ans_list[0] = R[1]
ans_list[-1] = L[-2]

for a_idx in range(1,len(A)-1):
    ans_list[a_idx] = gcd(L[a_idx-1],R[a_idx+1])
    
print(max(ans_list))