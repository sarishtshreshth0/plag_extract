#約数全部
def Divisors(N):
    N=abs(N)
    L,U=[],[]
    k=1
    while k*k <=N:
        if N%k== 0:
            L.append(k)
            if k!=N//k:
                U.append(N//k)
        k+=1
    return L+U[::-1]

def f(A,B):
    M=max(A,B)
    return len(str(M))
#================================================
N=int(input())
L=Divisors(N)
Y=float("inf")
for a in L:
    Y=min(Y,f(a,N//a))
print(Y)