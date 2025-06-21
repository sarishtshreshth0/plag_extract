import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=998244353
    N=I()
    D=LI()
    L=[0]*N
    N2=max(D)

    
    for i in range(N):
        L[D[i]]+=1
    prev=1
    ans=1
    if D[0]!=0 or L[0]!=1:
        print(0)
    else:
        for i in range(1,N2+1):
            now=L[i]
            ans=(ans*pow(prev,now,mod))%mod
            prev=now
            
        print(ans)
            
        
    

main()
