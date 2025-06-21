from math import inf

Q,H,S,D=map(int,input().split())
N=int(input())

L=inf
M=inf
for a in range(8+1):
    for b in range(4+1):
        for c in range(2+1):
            for d in range(1+1):
                if a+2*b+4*c+8*d==8:
                    L=min(L,a*Q+b*H+c*S+d*D)
                    
            if a+2*b+4*c==4:
                M=min(M,a*Q+b*H+c*S)

if N%2:
    print(L*(N//2)+M)
else:
    print(L*(N//2))
